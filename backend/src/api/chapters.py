from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import asc
import logging

from ..models import TextbookChapter
from ..models.database import get_db
from ..utils.logging import logger
from ..utils.error_handlers import create_error_response

router = APIRouter()

# Pydantic models for response types
from pydantic import BaseModel
from typing import Optional
import uuid

class ChapterBase(BaseModel):
    title: str
    slug: str
    order: int
    section: Optional[str] = None
    word_count: Optional[int] = 0
    reading_time: Optional[int] = 0

class ChapterResponse(ChapterBase):
    id: str

    class Config:
        from_attributes = True

class ChapterWithContent(ChapterResponse):
    content: str

class ChapterListResponse(BaseModel):
    chapters: List[ChapterResponse]
    total: int

@router.get("/", response_model=ChapterListResponse)
def get_all_chapters(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve a list of all textbook chapters
    """
    try:
        chapters = db.query(TextbookChapter).order_by(asc(TextbookChapter.order)).offset(skip).limit(limit).all()
        total = db.query(TextbookChapter).count()

        chapter_responses = [
            ChapterResponse(
                id=str(chapter.id),
                title=chapter.title,
                slug=chapter.slug,
                order=chapter.order,
                section=chapter.section,
                word_count=chapter.word_count,
                reading_time=chapter.reading_time
            ) for chapter in chapters
        ]

        logger.info(f"Retrieved {len(chapter_responses)} chapters")

        return ChapterListResponse(chapters=chapter_responses, total=total)

    except Exception as e:
        logger.error(f"Error retrieving chapters: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=create_error_response("DATABASE_ERROR", "Failed to retrieve chapters")
        )


@router.get("/{chapter_id}", response_model=ChapterResponse)
def get_chapter(
    chapter_id: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve a specific textbook chapter by ID
    """
    try:
        # Validate UUID format
        try:
            uuid.UUID(chapter_id)
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=create_error_response("INVALID_ID", "Invalid chapter ID format")
            )

        chapter = db.query(TextbookChapter).filter(TextbookChapter.id == chapter_id).first()

        if not chapter:
            raise HTTPException(
                status_code=404,
                detail=create_error_response("CHAPTER_NOT_FOUND", f"Chapter with ID {chapter_id} not found")
            )

        logger.info(f"Retrieved chapter: {chapter.title}")

        return ChapterResponse(
            id=str(chapter.id),
            title=chapter.title,
            slug=chapter.slug,
            order=chapter.order,
            section=chapter.section,
            word_count=chapter.word_count,
            reading_time=chapter.reading_time
        )

    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logger.error(f"Error retrieving chapter {chapter_id}: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=create_error_response("DATABASE_ERROR", "Failed to retrieve chapter")
        )


@router.get("/slug/{slug}", response_model=ChapterResponse)
def get_chapter_by_slug(
    slug: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve a specific textbook chapter by slug
    """
    try:
        chapter = db.query(TextbookChapter).filter(TextbookChapter.slug == slug).first()

        if not chapter:
            raise HTTPException(
                status_code=404,
                detail=create_error_response("CHAPTER_NOT_FOUND", f"Chapter with slug '{slug}' not found")
            )

        logger.info(f"Retrieved chapter by slug: {chapter.title}")

        return ChapterResponse(
            id=str(chapter.id),
            title=chapter.title,
            slug=chapter.slug,
            order=chapter.order,
            section=chapter.section,
            word_count=chapter.word_count,
            reading_time=chapter.reading_time
        )

    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logger.error(f"Error retrieving chapter with slug '{slug}': {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=create_error_response("DATABASE_ERROR", "Failed to retrieve chapter")
        )


@router.get("/{chapter_id}/content", response_model=ChapterWithContent)
def get_chapter_content(
    chapter_id: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve the content of a specific textbook chapter by ID
    """
    try:
        # Validate UUID format
        try:
            uuid.UUID(chapter_id)
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=create_error_response("INVALID_ID", "Invalid chapter ID format")
            )

        chapter = db.query(TextbookChapter).filter(TextbookChapter.id == chapter_id).first()

        if not chapter:
            raise HTTPException(
                status_code=404,
                detail=create_error_response("CHAPTER_NOT_FOUND", f"Chapter with ID {chapter_id} not found")
            )

        logger.info(f"Retrieved chapter content: {chapter.title}")

        return ChapterWithContent(
            id=str(chapter.id),
            title=chapter.title,
            slug=chapter.slug,
            order=chapter.order,
            section=chapter.section,
            word_count=chapter.word_count,
            reading_time=chapter.reading_time,
            content=chapter.content
        )

    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logger.error(f"Error retrieving chapter content {chapter_id}: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=create_error_response("DATABASE_ERROR", "Failed to retrieve chapter content")
        )


@router.get("/slug/{slug}/content", response_model=ChapterWithContent)
def get_chapter_content_by_slug(
    slug: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve the content of a specific textbook chapter by slug
    """
    try:
        chapter = db.query(TextbookChapter).filter(TextbookChapter.slug == slug).first()

        if not chapter:
            raise HTTPException(
                status_code=404,
                detail=create_error_response("CHAPTER_NOT_FOUND", f"Chapter with slug '{slug}' not found")
            )

        logger.info(f"Retrieved chapter content by slug: {chapter.title}")

        return ChapterWithContent(
            id=str(chapter.id),
            title=chapter.title,
            slug=chapter.slug,
            order=chapter.order,
            section=chapter.section,
            word_count=chapter.word_count,
            reading_time=chapter.reading_time,
            content=chapter.content
        )

    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logger.error(f"Error retrieving chapter content with slug '{slug}': {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=create_error_response("DATABASE_ERROR", "Failed to retrieve chapter content")
        )