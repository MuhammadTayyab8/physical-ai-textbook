from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from .logging import logger
from typing import Dict, Any
import traceback


async def http_exception_handler(request: Request, exc: HTTPException):
    """Global HTTP exception handler"""
    logger.error(f"HTTP Exception: {exc.status_code} - {exc.detail}")
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "type": "HTTPException",
                "code": exc.status_code,
                "message": exc.detail
            }
        }
    )


async def validation_exception_handler(request: Request, exc: Exception):
    """Global request validation exception handler"""
    logger.error(f"Validation Exception: {str(exc)}")
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "type": "ValidationError",
                "code": "VALIDATION_ERROR",
                "message": "Request validation failed",
                "details": str(exc)
            }
        }
    )


async def general_exception_handler(request: Request, exc: Exception):
    """Global general exception handler"""
    logger.error(f"General Exception: {str(exc)}")
    logger.debug(f"Traceback: {traceback.format_exc()}")
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": {
                "type": "InternalServerError",
                "code": "INTERNAL_ERROR",
                "message": "An internal server error occurred"
            }
        }
    )


def create_error_response(error_type: str, message: str, details: Any = None) -> Dict[str, Any]:
    """Create a standardized error response"""
    error_response = {
        "error": {
            "type": error_type,
            "message": message
        }
    }
    
    if details:
        error_response["error"]["details"] = details
    
    return error_response