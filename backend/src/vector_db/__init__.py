from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import Optional, List, Dict, Any
import logging
from ..config import settings

logger = logging.getLogger(__name__)

class QdrantConfig:
    def __init__(self):
        # Initialize the Qdrant client
        self.client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
            prefer_grpc=False  # Using HTTP for simplicity, but gRPC can be faster
        )
        
        # Define collection name for textbook content
        self.content_collection_name = "textbook_content"
        self.question_answer_collection_name = "qa_pairs"
        
        # Initialize collections if they don't exist
        self._init_collections()
    
    def _init_collections(self):
        """Initialize collections if they don't exist"""
        try:
            # Check if content collection exists, if not create it
            collections = self.client.get_collections().collections
            collection_names = [coll.name for coll in collections]
            
            if self.content_collection_name not in collection_names:
                self.client.create_collection(
                    collection_name=self.content_collection_name,
                    vectors_config=models.VectorParams(
                        size=1536,  # Default OpenAI embedding size
                        distance=models.Distance.COSINE
                    )
                )
                logger.info(f"Created Qdrant collection: {self.content_collection_name}")
            
            if self.question_answer_collection_name not in collection_names:
                self.client.create_collection(
                    collection_name=self.question_answer_collection_name,
                    vectors_config=models.VectorParams(
                        size=1536,  # Default OpenAI embedding size
                        distance=models.Distance.COSINE
                    )
                )
                logger.info(f"Created Qdrant collection: {self.question_answer_collection_name}")
                
        except Exception as e:
            logger.error(f"Error initializing Qdrant collections: {e}")
            raise
    
    def get_client(self):
        """Return the Qdrant client instance"""
        return self.client

# Global instance
qdrant_config = QdrantConfig()