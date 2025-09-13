from fastapi import FastAPI
from services.pdf_service.controller import router as upload_router

app = FastAPI()
app.include_router(upload_router)

@app.get("/health")
def health():
    return {"message" : "API is running!"}