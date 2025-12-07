from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, UUID, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from .database import Base


class TextbookChapter(Base):
    __tablename__ = "textbook_chapters"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    slug = Column(String(200), nullable=False, unique=True)
    order = Column(Integer, nullable=False)
    section = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    word_count = Column(Integer, default=0)
    reading_time = Column(Integer, default=0)  # Estimated reading time in minutes

    # Relationship
    content_blocks = relationship("ContentBlock", back_populates="chapter")


class ContentBlock(Base):
    __tablename__ = "content_blocks"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chapter_id = Column(PG_UUID(as_uuid=True), ForeignKey("textbook_chapters.id"), nullable=False)
    type = Column(String(50), nullable=False)  # paragraph, code, figure, table
    content = Column(Text, nullable=False)
    position = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    vector_id = Column(String(100), nullable=False)  # Reference to Qdrant vector ID

    # Relationship
    chapter = relationship("TextbookChapter", back_populates="content_blocks")


class UserQuestion(Base):
    __tablename__ = "user_questions"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question = Column(Text, nullable=False)
    user_id = Column(String(100), nullable=True)  # Optional user identifier
    session_id = Column(String(100), nullable=False)  # Session identifier for conversation context
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # JSON field for storing content block IDs used in the response
    relevant_content_ids = Column(Text, nullable=True)  # Store as JSON string


class RAGResponse(Base):
    __tablename__ = "rag_responses"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column(PG_UUID(as_uuid=True), ForeignKey("user_questions.id"), nullable=False)
    response = Column(Text, nullable=False)
    # JSON field for storing source content block IDs
    sources = Column(Text, nullable=False)  # Store as JSON string
    confidence = Column(Float, nullable=False)  # Confidence score 0.0-1.0
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    feedback = Column(Text, nullable=True)  # Optional user feedback on response quality

    # Relationship
    question = relationship("UserQuestion")


class SearchQuery(Base):
    __tablename__ = "search_queries"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    query = Column(String(500), nullable=False)
    user_id = Column(String(100), nullable=True)  # Optional user identifier
    session_id = Column(String(100), nullable=False)
    # JSON field for storing results
    results = Column(Text, nullable=False)  # Store as JSON string
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class UserSession(Base):
    __tablename__ = "user_sessions"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String(100), nullable=True)  # Optional user identifier
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_activity_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)