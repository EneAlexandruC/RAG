from fastapi import APIRouter, UploadFile, File, HTTPException
from services.pdf_service.config import supabase, SUPABASE_BUCKET
from services.pdf_service.helper import extract_text_from_pdf, chunk_text, store_embeddings
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File()):
    """ Upload a PDF, extract text, create embeddings, store in Supabase """

    if not file.filename or not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed.")
    file_bytes = await file.read()

    # Upload file to supabase storage
    file_path = f"{file.filename}"
    res = supabase.storage.from_(SUPABASE_BUCKET).upload(file_path, file_bytes)

    if res.get("error"):
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