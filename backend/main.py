from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional, List
import os
from dotenv import load_dotenv
import sys
from pathlib import Path

# Add the backend directory to the Python path
backend_path = Path(__file__).parent
sys.path.insert(0, str(backend_path))

# Load environment variables
load_dotenv()

app = FastAPI(
    title="RAG Chatbot API",
    description="Backend for RAG Chatbot System with OpenAI Agents",
    version="0.1.0"
)

# Add CORS middleware to allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str
    sources: Optional[List[Dict[str, Any]]] = []

class EmbeddingRequest(BaseModel):
    textbook_url: str

class EmbeddingResponse(BaseModel):
    message: str
    chunks_processed: int

# Global instances
rag_agent = None
textbook_embedder = None

@app.on_event("startup")
async def startup_event():
    """Initialize the RAG agent and textbook embedder on startup"""
    global rag_agent, textbook_embedder
    from src.agents.rag_agent import RAGAgent
    from src.embeddings.textbook_embedder import TextbookEmbedder
    
    rag_agent = RAGAgent()
    textbook_embedder = TextbookEmbedder()

@app.get("/")
async def root():
    return {"message": "RAG Chatbot Backend API", "status": "running"}

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    """
    Main endpoint to process user queries using OpenAI Agents with RAG capabilities
    """
    global rag_agent

    if not rag_agent:
        raise HTTPException(status_code=500, detail="RAG agent not initialized")

    try:
        # Process the query using the RAG agent
        result = rag_agent.query(request.query)

        return QueryResponse(
            response=result["response"],
            sources=result.get("sources", [])
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.post("/embed-textbook", response_model=EmbeddingResponse)
async def embed_textbook_endpoint(request: EmbeddingRequest):
    """
    Endpoint to embed a textbook from a URL into the vector store
    """
    global textbook_embedder

    if not textbook_embedder:
        raise HTTPException(status_code=500, detail="Textbook embedder not initialized")

    try:
        # Process embedding
        chunks_processed = await textbook_embedder.embed_and_store_textbook(request.textbook_url)

        return EmbeddingResponse(
            message="Textbook successfully embedded",
            chunks_processed=chunks_processed
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error embedding textbook: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "RAG Chatbot Backend API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)