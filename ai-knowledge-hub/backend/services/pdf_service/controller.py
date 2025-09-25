from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from typing import List, Optional   
from services.config import supabase, SUPABASE_BUCKET, client
from services.pdf_service.helper import *
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/search")
async def search_pdfs(query = Query(...), top_k: int = 5, document_ids: Optional[List[str]] = Query(None)):
    """ Search for relevant chunks in the database then returns the processed message"""

    context_chunks = search_documents(query, top_k, document_ids)

    context_text = "\n".join([chunk["content"] for chunk in context_chunks])

    prompt = f"""
    Context:
    {context_text}

    Question: {query}
    Answer concisely based only on the context.
    """

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
    )

    answer = completion.choices[0].message.content

    save_qa(query, answer, document_ids)

    return {
        "question": query,
        "context_used": context_chunks,
        "answer": answer
    } 

@router.post("/upload")
async def upload_pdf(file: UploadFile = File()):
    """ Upload a PDF, extract text, create embeddings, store in Supabase """

    if not file.filename or not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed.")
    file_bytes = await file.read()

    # Upload file to supabase storage
    file_path = f"{file.filename}"
    res = supabase.storage.from_(SUPABASE_BUCKET).upload(file_path, file_bytes)

    if not res:
        raise HTTPException(status_code=500, detail=f"Supabase upload failed: {res['error']}")
    
    # Create a document entry
    response = supabase.table("documents").insert({"file_name": file.filename}).execute()

    if response.data is None:
        raise HTTPException(status_code=500, detail="Document entry failed")
    document_id = response.data[0]["id"]

    # Extract text + chunk it
    text = extract_text_from_pdf(file_bytes)
    chunks = chunk_text(text)

    # Generate embeddings + store
    count = store_embeddings(document_id, chunks)

    return JSONResponse(content={
        "message": "PDF processed successfully",
        "document_id": document_id,
        "chunks_indexed": count
    })