import os
import requests
from fastapi import FastAPI, Query, HTTPException
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

app = FastAPI(title="Dynamic News RAG Bot")

# --------------------
# Health Check
# --------------------
@app.get("/health")
def health():
    return {"ok": True}

# --------------------
# Fetch News from GNews
# --------------------
def fetch_news():
    url = "https://gnews.io/api/v4/top-headlines"
    params = {
        "lang": "en",
        "max": 5,
        "apikey": GNEWS_API_KEY
    }

    r = requests.get(url, params=params, timeout=30)

    if r.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail=f"GNews error {r.status_code}: {r.text}"
        )

    articles = r.json().get("articles", [])
    if not articles:
        return "No news available."

    return "\n".join(
        f"- {a['title']}: {a.get('description','')}"
        for a in articles
    )

# --------------------
# Ask Ollama
# --------------------
def ask_ollama(prompt: str) -> str:
    r = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    if r.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail=f"Ollama error {r.status_code}: {r.text}"
        )

    return r.json()["response"]

# --------------------
# Ask Endpoint
# --------------------
@app.get("/ask")
def ask(q: str = Query(...)):
    news = fetch_news()

    prompt = f"""
You are a news assistant.

Latest headlines:
{news}

User question:
{q}

Give a concise answer based on the news.
"""

    answer = ask_ollama(prompt)

    return {
        "question": q,
        "answer": answer,
        "source": "GNews + Ollama"
    }
