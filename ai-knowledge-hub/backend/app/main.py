from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.pdf_service.controller import router as upload_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(upload_router)

@app.get("/health")
def health():
    return {"message" : "API is running!"}