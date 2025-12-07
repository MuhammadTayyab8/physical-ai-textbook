import logging
from logging.handlers import RotatingFileHandler
import os
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from typing import Optional
import traceback
import sys
from ..config import settings


def setup_logging():
    """Configure application logging"""
    # Create logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if settings.debug else logging.INFO)
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )
    simple_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG if settings.debug else logging.INFO)
    console_handler.setFormatter(simple_formatter)
    
    # Create file handler with rotation
    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(detailed_formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger


def get_logger(name: str) -> logging.Logger:
    """Get a named logger instance"""
    return logging.getLogger(name)


# Set up the main logger
logger = setup_logging()


class TextbookException(HTTPException):
    """Custom exception for textbook-related errors"""
    def __init__(self, status_code: int, detail: str, error_code: Optional[str] = None):
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code or f"TEXTBOOK_ERROR_{status_code}"


class ContentNotFoundException(TextbookException):
    """Raised when requested content is not found"""
    def __init__(self, detail: str = "Content not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
            error_code="CONTENT_NOT_FOUND"
        )


class RAGException(TextbookException):
    """Raised when RAG operations fail"""
    def __init__(self, detail: str = "RAG operation failed"):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            error_code="RAG_ERROR"
        )


def handle_error(error: Exception, logger: logging.Logger, context: str = ""):
    """Generic error handling function"""
    error_msg = f"Error in {context}: {str(error)}"
    logger.error(error_msg, exc_info=True)
    
    # Log the full traceback for debugging
    if settings.debug:
        logger.debug("Full traceback:\n" + traceback.format_exc())
    
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "type": type(error).__name__,
                "message": str(error),
                "context": context
            }
        }
    )


def log_api_call(endpoint: str, method: str, user_id: Optional[str] = None):
    """Decorator to log API calls"""
    def decorator(func):
        async def wrapper(*args, **kwargs):
            logger.info(f"API Call: {method} {endpoint} - User: {user_id}")
            try:
                result = await func(*args, **kwargs)
                logger.info(f"API Success: {method} {endpoint}")
                return result
            except Exception as e:
                logger.error(f"API Error: {method} {endpoint} - {str(e)}")
                raise
        return wrapper
    return decorator