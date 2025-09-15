import os
from dotenv import load_dotenv
from supabase import create_client
from sentence_transformers import SentenceTransformer
from groq import Groq

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET", "documents")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not SUPABASE_URL or not SUPABASE_API_KEY:
    raise TypeError("SUPABASE_API_KEY | SUPABASE_URL are None")

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

client = Groq(api_key=GROQ_API_KEY)

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

