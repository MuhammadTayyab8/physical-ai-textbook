from fastapi import APIRouter
from . import chapters, chat, search

# Main API router
api_router = APIRouter()

# Include all API routes
api_router.include_router(chapters.router, prefix="/chapters", tags=["chapters"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(search.router, prefix="/search", tags=["search"])

# Health check endpoint
@api_router.get("/health", tags=["health"])
def health_check():
    return {"status": "healthy", "service": "textbook-api"}

# Root endpoint
@api_router.get("/", tags=["root"])
def read_root():
    return {
        "message": "Physical AI & Humanoid Robotics Textbook API",
        "version": "1.0.0",
        "endpoints": [
            "/chapters",
            "/chat",
            "/search",
            "/health"
        ]
    }