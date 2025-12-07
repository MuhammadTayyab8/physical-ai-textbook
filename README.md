# Physical AI & Humanoid Robotics Textbook

Welcome to the Physical AI & Humanoid Robotics Textbook project! This is a comprehensive educational resource combined with an AI-powered chatbot that leverages the textbook content to answer questions.

## Overview

This project consists of:
- A Docusaurus-based frontend for the textbook content
- A FastAPI backend with RAG (Retrieval-Augmented Generation) capabilities
- Qdrant vector database for content indexing
- PostgreSQL for metadata storage

## Features

- **Textbook Content**: Comprehensive chapters on Physical AI and Humanoid Robotics
- **AI-Powered Q&A**: Ask questions about the textbook content and get AI-generated answers
- **Search Functionality**: Search through textbook content using keywords
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Fast Loading**: Optimized for performance and quick access

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Textbook      │    │   FastAPI        │    │   PostgreSQL    │
│   Frontend      │───▶│   Backend        │───▶│   Database      │
│   (Docusaurus)  │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                            │    ▲
                            │    │
                            ▼    │
                       ┌─────────────┐
                       │   Qdrant    │
                       │ Vector DB   │
                       └─────────────┘
```

## Prerequisites

- Node.js (v18 or higher)
- Python (v3.11 or higher)
- Docker and Docker Compose
- OpenAI API key
- (Optional) Qdrant API key if using hosted Qdrant

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-organization/physical-ai-textbook.git
cd physical-ai-textbook
```

### 2. Environment Configuration

Create a `.env` file in the project root with your API keys:

```bash
# Copy the example file
cp .env.example .env

# Edit the file with your actual keys
OPENAI_API_KEY=your_openai_api_key_here
QDRANT_URL=http://qdrant:6333  # Default for Docker setup
QDRANT_API_KEY=your_qdrant_api_key_here  # If using hosted Qdrant
DATABASE_URL=postgresql://textbook_user:textbook_password@db:5432/textbook_db
```

### 3. Initialize the Development Environment

Use Docker Compose to set up all services:

```bash
# Start all services (Docusaurus frontend, FastAPI backend, Qdrant, PostgreSQL)
docker-compose up --build
```

Wait for all services to start. The frontend will be available at `http://localhost:3000` and the backend API at `http://localhost:8000`.

## Running the Application

### Development Mode

To work with the application in development mode:

1. Start all services with Docker Compose:
   ```bash
   docker-compose up
   ```

2. Access the textbook at `http://localhost:3000`
3. Access the API documentation at `http://localhost:8000/docs`

### Adding New Textbook Content

To add new chapters to the textbook:

1. Create a new Markdown file in the `textbook/docs/` directory
2. Add the file to the `textbook/sidebars.js` configuration
3. Rebuild the vector database with the new content:
   ```bash
   # From the project root
   python scripts/vectorize.py
   ```

## API Endpoints

The backend API provides the following endpoints:

- `GET /api/v1/chapters/` - Get a list of all textbook chapters
- `GET /api/v1/chapters/{chapter_id}` - Get a specific chapter's metadata
- `GET /api/v1/chapters/{chapter_id}/content` - Get a specific chapter's content
- `GET /api/v1/chapters/slug/{slug}` - Get a specific chapter by slug
- `GET /api/v1/chapters/slug/{slug}/content` - Get a specific chapter's content by slug
- `POST /api/v1/chat/` - Ask questions about the textbook content
- `GET /api/v1/search/` - Search through textbook content

## Project Structure

```
physical-ai-textbook/
├── textbook/                 # Docusaurus frontend
│   ├── docs/                 # Textbook content (Markdown)
│   ├── src/                  # Custom components and styling
│   ├── static/               # Static assets
│   ├── package.json          # Frontend dependencies
│   └── docusaurus.config.js  # Docusaurus configuration
├── backend/                  # FastAPI backend
│   ├── src/                  # Backend source code
│   │   ├── models/           # Database models
│   │   ├── services/         # Business logic
│   │   ├── api/              # API endpoints
│   │   └── lib/              # Utility functions
│   ├── requirements.txt      # Python dependencies
│   └── main.py               # FastAPI application entry point
├── scripts/                  # Utility scripts
│   └── vectorize.py          # Content vectorization script
├── vector-db/                # Vector database configuration
├── deployment/               # Deployment configurations
├── specs/                    # Feature specifications
└── docker-compose.yml        # Docker configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please file an issue in the GitHub repository.