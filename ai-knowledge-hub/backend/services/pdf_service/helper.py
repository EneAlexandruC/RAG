from pypdf import PdfReader
from services.config import supabase, embedder
from fastapi import HTTPException
import numpy as np
import io
import ast

def save_qa(question, answer, document_ids = None):
    """ Save QA and link it with one or more documents """

    response = supabase.table("qa_history").insert({
        "question": question,
        "answer": answer
    }).execute()

    if not response.data:
        raise HTTPException(status_code=500, detail="Failed to save QA pair")
    
    qa_id = response.data[0]["id"]

    if document_ids:
        links = [{"qa_id": qa_id, "document_id": doc_id} for doc_id in document_ids]
        supabase.table("qa_documents").insert(links).execute()

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def search_documents(query, top_k = 5, document_ids = None):
    """ Search for the most relevant chunks given a text query """

    query_embedding = embedder.encode([query])[0]

    sb_query = supabase.table("chunks").select("id, content, embedding, document_id")

    if document_ids:
        sb_query = sb_query.in_("document_id", document_ids)
    response = sb_query.execute()

    if not response.data:
        return []

    # Compute similarity
    scored_results = []
    for row in response.data:
        embedding = row["embedding"]
        if isinstance(embedding, str):
            embedding = ast.literal_eval(embedding)

        db_embedding = np.array(embedding, dtype=np.float32)
        score = cosine_similarity(query_embedding, db_embedding)
        scored_results.append({
            "id": row["id"],
            "document_id": row["document_id"],
            "content": row["content"],
            "score": float(score)
        })

    # Sort descending after the score
    scored_results.sort(key=lambda x: x["score"], reverse=True)
    return scored_results[:int(top_k)]

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