from fastapi import FastAPI
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key = api_key)

app = FastAPI()

@app.get("/test-gpt")
def test_gpt():
    response = client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Reply with a short motivational quote"}
        ]
    )

    return {"quote": response.choices[0].message.content}