import re
from typing import List, Dict, Any, Tuple
import hashlib
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def extract_text_from_markdown(markdown_content: str) -> str:
    """
    Extract plain text from markdown content by removing markdown syntax
    while preserving the actual content
    """
    # Remove markdown headers but keep the text
    text = re.sub(r'^#+\s*', '', markdown_content, flags=re.MULTILINE)
    
    # Remove emphasis markers but keep the text
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Bold with **
    text = re.sub(r'__(.*?)__', r'\1', text)      # Bold with __
    text = re.sub(r'\*(.*?)\*', r'\1', text)      # Italic with *
    text = re.sub(r'_(.*?)_', r'\1', text)        # Italic with _
    
    # Remove links but keep the text: [text](url) -> text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    
    # Remove images but keep alt text: ![alt](url) -> alt
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', text)
    
    # Remove code blocks and inline code
    text = re.sub(r'```.*?\n```', '', text, flags=re.DOTALL)  # Fenced code blocks
    text = re.sub(r'`([^`]+)`', r'\1', text)  # Inline code
    
    # Remove horizontal rules
    text = re.sub(r'^\s*[-*_]{3,}\s*$', '', text, flags=re.MULTILINE)
    
    # Remove blockquotes
    text = re.sub(r'^\s*>\s?', '', text, flags=re.MULTILINE)
    
    # Normalize whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)  # Multiple blank lines to single
    text = text.strip()
    
    return text

def chunk_text(text: str, max_chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Split text into overlapping chunks of approximately max_chunk_size
    """
    if len(text) <= max_chunk_size:
        return [text]
    
    chunks = []
    start = 0
    
    while start < len(text):
        # Find the end position
        end = start + max_chunk_size
        
        # If we're at the end, take the remaining text
        if end >= len(text):
            chunks.append(text[start:])
            break
        
        # Try to break at a sentence boundary near the end
        chunk = text[start:end]
        
        # Find the last sentence end in the chunk
        sentence_end = max(
            chunk.rfind('. '),
            chunk.rfind('?'),
            chunk.rfind('!'),
            chunk.rfind('\n')
        )
        
        # If we found a good sentence break point, use it
        if sentence_end > max_chunk_size // 2:  # Make sure we're not cutting too early
            actual_end = start + sentence_end + 1
            chunks.append(text[start:actual_end])
            start = actual_end - overlap  # Overlap with previous chunk
        else:
            # If no sentence break found, just take the max chunk size
            chunks.append(text[start:end])
            start = end - overlap
        
        # Ensure we make progress even if we're stuck
        if start <= chunks[-1]:
            start += 1
    
    # Filter out empty chunks
    return [chunk for chunk in chunks if chunk.strip()]

def generate_content_id(content: str, prefix: str = "content") -> str:
    """
    Generate a unique ID for content based on its content hash
    """
    content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
    return f"{prefix}_{content_hash}"

def calculate_reading_time(text: str, words_per_minute: int = 200) -> int:
    """
    Calculate estimated reading time in minutes based on word count
    """
    words = len(text.split())
    minutes = words / words_per_minute
    return max(1, round(minutes))  # At least 1 minute

def sanitize_content(content: str) -> str:
    """
    Sanitize content by removing potentially harmful code or scripts
    """
    # Use BeautifulSoup to remove script and style elements
    soup = BeautifulSoup(content, 'html.parser')
    
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()
    
    # Get text and return
    return soup.get_text()

def detect_content_type(content: str) -> str:
    """
    Detect the type of content (text, code, math, etc.)
    """
    # Check for code blocks (indented or fenced)
    if '```' in content or '\n    ' in content:
        return "code"
    
    # Check for math expressions
    if re.search(r'\$.*?\$|\$\$.*?\$\$', content):
        return "math"
    
    # Check for tables
    if re.search(r'\|.*?\|', content):
        return "table"
    
    # Default to paragraph
    return "paragraph"

def extract_chapter_metadata(content: str) -> Dict[str, Any]:
    """
    Extract metadata from chapter content like headings, word count, etc.
    """
    metadata = {
        "headings": [],
        "word_count": 0,
        "paragraphs": 0,
        "code_blocks": 0,
        "word_count_reading_time": 0
    }
    
    # Count words
    metadata["word_count"] = len(content.split())
    
    # Count paragraphs (separated by double newlines)
    paragraphs = content.split('\n\n')
    metadata["paragraphs"] = len([p for p in paragraphs if p.strip()])
    
    # Count code blocks
    metadata["code_blocks"] = len(re.findall(r'```.*?```', content, re.DOTALL))
    
    # Extract headings
    heading_pattern = r'^(#{1,6})\s+(.*)$'
    matches = re.findall(heading_pattern, content, re.MULTILINE)
    metadata["headings"] = [{"level": len(h[0]), "title": h[1].strip()} for h in matches]
    
    # Calculate reading time
    metadata["word_count_reading_time"] = calculate_reading_time(content)
    
    return metadata