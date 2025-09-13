import os
from dotenv import load_dotenv
from supabase import create_client
from sentence_transformers import SentenceTransformer

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET", "documents")

if not SUPABASE_URL or not SUPABASE_API_KEY:
    raise TypeError("SUPABASE_API_KEY | SUPABASE_URL are None")

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

