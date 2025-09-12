# AI Knowledge Hub

## Overview

AI Knowledge Hub is a web application that allows users to upload documents (PDFs) and ask questions about their content using advanced AI. The project combines **retrieval-augmented generation (RAG)** with state-of-the-art LLMs and embeddings to provide accurate and context-aware answers.

The main goal is to create a system where:

- Users upload documents.
- Documents are converted into embeddings for semantic search.
- Users can ask natural language questions.
- The AI responds accurately using the relevant sections from the documents.

**This project is intended for personal learning.**

---

### Core Functionality

- **Document Upload**: Users can upload PDFs for processing.
- **Embeddings Generation**: Convert document text into vector embeddings using HuggingFace `sentence-transformers`.
- **Semantic Search**: Search through embeddings to retrieve relevant passages for questions.
- **AI Chat**: Ask questions in natural language and receive answers using Groq LLMs (e.g., `openai/gpt-oss-20b`).
- **Retrieval-Augmented Generation (RAG)**: Combines retrieved passages with AI model to generate context-aware answers.
- **FastAPI Backend**: Handles API requests for uploads, embedding generation, and AI queries.
- **Web Frontend**: (Planned) React or another modern framework to interact with the system via browser.

### Extra Features / Roadmap

- **User Authentication**: Secure login/logout for multiple users.
- **Document Management**: Keep track of uploaded documents for each user.
- **History Logging**: Save past questions and AI responses.
- **Multiple Model Support**: Easily switch between AI models (Groq, local models, OpenAI) and embeddings.
- **Deployment Ready**: Can be deployed on Render, Railway, or other cloud platforms.
- **Error Handling & Logging**: Gracefully handle errors and log system events for debugging.

## Tech Stack

- **Backend**: Python, FastAPI, Uvicorn
- **AI Models**: Groq (LLM for QA), HuggingFace Sentence Transformers (for embeddings)
- **Database / Storage**: ChromaDB (local vector database) or alternative vector DB
- **Frontend**: React (planned)
- **Environment**: Python virtual environment (`venv`)
- **Other Tools**: dotenv for environment variables, Postman for API testing

## Architecture Overview

### Can be found in docs/architecture-flowchart!

## Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/EneAlexandruC/RAG.git
cd ai-knowledge-hub
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file in the root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run Backend Server

```bash
uvicorn main:app --reload
```

## Contribution

Contributions are welcome!

- **Add new AI models or embeddings**
- **Improve frontend UI**
- **Add user authentication**
- **Optimize RAG pipeline**
