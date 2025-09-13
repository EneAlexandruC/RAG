from pypdf import PdfReader
from services.pdf_service.config import supabase, embedder
from fastapi import HTTPException
import io
import json

def extract_text_from_pdf(file_bytes):
    """ Extract text from a PDF file (bytes) """

    reader = PdfReader(io.BytesIO(file_bytes))
    text = ""

    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text

def chunk_text(text, chunk_size = 500):
    """ Split text into smaller chunks by words """

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def store_embeddings(document_id, chunks):
    """ Generate embeddings and store in Supabase """

    embeddings = embedder.encode(chunks)
    rows = []

    for chunk, embedding in zip(chunks, embeddings):
        rows.append({
            "document_id": document_id,
            "content": chunk,
            "embedding": embedding.tolist()
        })

    try:
        supabase.table("chunks").insert(rows).execute()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Supabase insert failed: {str(e)}")

    return len(rows)