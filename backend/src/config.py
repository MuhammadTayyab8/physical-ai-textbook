from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    # Database settings
    database_url: str = os.getenv("DATABASE_URL", "postgresql://textbook_user:textbook_password@localhost/textbook_db")
    
    # OpenAI settings
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    # Qdrant settings
    qdrant_url: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    qdrant_api_key: Optional[str] = os.getenv("QDRANT_API_KEY")
    
    # Application settings
    app_name: str = "Physical AI & Humanoid Robotics Textbook API"
    app_version: str = "1.0.0"
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    environment: str = os.getenv("ENVIRONMENT", "development")
    
    # API settings
    allowed_origins: str = os.getenv("ALLOWED_ORIGINS", "*")
    api_prefix: str = "/api/v1"
    
    # Content settings
    max_content_chunk_size: int = int(os.getenv("MAX_CONTENT_CHUNK_SIZE", "1000"))
    min_content_chunk_size: int = int(os.getenv("MIN_CONTENT_CHUNK_SIZE", "100"))
    
    class Config:
        case_sensitive = True

# Create a single instance of settings
settings = Settings()

# Validate that required settings exist
def validate_settings():
    errors = []
    if not settings.openai_api_key:
        errors.append("OPENAI_API_KEY is required")
    if not settings.qdrant_url:
        errors.append("QDRANT_URL is required")
    
    if errors:
        raise ValueError(f"Configuration errors: {'; '.join(errors)}")

# Run validation when module is loaded
validate_settings()