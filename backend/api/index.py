# api/index.py
import json
import os
from typing import Dict, Any
from urllib.parse import parse_qs
from dotenv import load_dotenv
import asyncio

# Import modules from the parent directory
import sys
from pathlib import Path
import importlib.util

# Add the backend directory to the Python path
backend_path = Path(__file__).parent.parent
sys.path.insert(0, str(backend_path))

# Load environment variables
load_dotenv()

from src.agents.rag_agent import RAGAgent
from src.embeddings.textbook_embedder import TextbookEmbedder

# Initialize agents globally for reuse
rag_agent = None
textbook_embedder = None

def init_agents():
    global rag_agent, textbook_embedder
    if rag_agent is None:
        rag_agent = RAGAgent()
    if textbook_embedder is None:
        textbook_embedder = TextbookEmbedder()

def handle_request(event, context):
    """Vercel serverless function entry point"""
    try:
        # Initialize agents if not already done
        init_agents()

        # Parse HTTP method and path
        http_method = event.get('httpMethod', '').upper()
        path = event.get('path', '')
        body = event.get('body', '')
        
        # Parse query parameters
        raw_query = event.get('rawQuery', '')
        query_params = parse_qs(raw_query) if raw_query else {}

        # Handle different routes
        if http_method == 'GET' and path == '/':
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({"message": "RAG Chatbot Backend API", "status": "running"})
            }
        elif http_method == 'GET' and path == '/health':
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({"status": "healthy", "message": "RAG Chatbot Backend API is running"})
            }
        elif http_method == 'POST' and path == '/query':
            # Parse the request body
            try:
                body_data = json.loads(body) if body else {}
                query = body_data.get('query', '')
                
                if not query:
                    return {
                        'statusCode': 400,
                        'headers': {'Content-Type': 'application/json'},
                        'body': json.dumps({"error": "Missing query parameter"})
                    }
                
                # Process the query using the RAG agent
                result = asyncio.run(rag_agent.query(query))
                
                return {
                    'statusCode': 200,
                    'headers': {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': '*',
                        'Access-Control-Allow-Headers': '*'
                    },
                    'body': json.dumps({
                        "response": result["response"],
                        "sources": result.get("sources", [])
                    })
                }
            except json.JSONDecodeError:
                return {
                    'statusCode': 400,
                    'headers': {'Content-Type': 'application/json'},
                    'body': json.dumps({"error": "Invalid JSON in request body"})
                }
        elif http_method == 'POST' and path == '/embed-textbook':
            # Parse the request body
            try:
                body_data = json.loads(body) if body else {}
                textbook_url = body_data.get('textbook_url', '')
                
                if not textbook_url:
                    return {
                        'statusCode': 400,
                        'headers': {'Content-Type': 'application/json'},
                        'body': json.dumps({"error": "Missing textbook_url parameter"})
                    }
                
                # Process textbook embedding
                chunks_processed = asyncio.run(textbook_embedder.embed_and_store_textbook(textbook_url))
                
                return {
                    'statusCode': 200,
                    'headers': {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Methods': '*',
                        'Access-Control-Allow-Headers': '*'
                    },
                    'body': json.dumps({
                        "message": "Textbook successfully embedded",
                        "chunks_processed": chunks_processed
                    })
                }
            except json.JSONDecodeError:
                return {
                    'statusCode': 400,
                    'headers': {'Content-Type': 'application/json'},
                    'body': json.dumps({"error": "Invalid JSON in request body"})
                }
        else:
            return {
                'statusCode': 404,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({"error": "Route not found"})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({"error": str(e)})
        }

# This is the function that Vercel will call
def main(event, context):
    return handle_request(event, context)

# Make the main handler available at module level
handler = main