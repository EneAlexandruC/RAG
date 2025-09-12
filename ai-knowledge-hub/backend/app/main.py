from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running!"}

@app.get("/health")
def health():
    return {"message" : "API is running!"}