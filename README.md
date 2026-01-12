# 📰 Dynamic RAG News Chatbot (Ollama + GNews)

A **Dynamic Retrieval-Augmented Generation (RAG) chatbot** that answers user questions using **live news data** from the **GNews API** and generates responses using a **local LLM via Ollama**.  
The system is fully containerized using **Docker Compose** and requires **no OpenAI API key**.

This project was built as part of a hackathon to demonstrate:
- Real-time data ingestion
- Dynamic knowledge retrieval
- Local LLM inference
- Cloud-ready deployment

---

## 🚀 What This Project Does

- Fetches **latest news in real time** using the GNews API
- Builds dynamic context from live articles
- Uses **Ollama (LLaMA 3.2)** to generate answers
- Responds instantly without re-indexing or restarting
- Runs fully inside Docker containers
- Exposes a clean REST API using FastAPI

---

## 🧠 Architecture Overview
User Query

↓

FastAPI (/ask endpoint)

↓

Fetch live news (GNews API)

↓

Dynamic prompt construction (RAG)

↓

Ollama (LLaMA 3.2)

↓

AI-generated response


---

## 🧱 Tech Stack

- FastAPI
- Python
- Ollama (LLaMA 3.2)
- GNews API
- Docker & Docker Compose

---

## 📁 Project Structure

dynamic-rag-chatbot/

│

├── app.py # FastAPI application

├── Dockerfile # Builds the ragbot container

├── docker-compose.yml # Runs Ollama + ragbot

├── requirements.txt # Python dependencies

├── .env # Environment variables (ignored by Git)

├── .gitignore # Git ignore rules

└── README.md # Project documentation

---

🔑 How to Get GNews API Key

1. Visit https://gnews.io
2. Sign up for a free account
3. Copy your API key
4. Paste it into the .env file

---
## 🐳 Docker Setup
Build and start the application
docker compose up -d --build

Verify running containers
docker compose ps

Expected services:
* ollama
* pathway-ragbot

---
## 🤖 Pull the Model (First Time Only)
docker exec -it ollama ollama pull llama3.2

Verify model:
docker exec -it ollama ollama list

---
## 🧪 API Endpoints
Health Check
GET /health

Example:
curl http://localhost:8000/health

Response:
{"ok": true}

Ask a Question
GET /ask?q=YOUR_QUESTION

Example (curl):
curl -G "http://localhost:8000/ask" \
  --data-urlencode "q=What is trending in the news today?"

Example (browser):
http://localhost:8000/ask?q=What%20is%20trending%20in%20the%20news%20today

Response:
{
  "question": "What is trending in the news today",
  "answer": "Based on the latest headlines...",
  "source": "GNews + Ollama"
}

---
## 🌐 GitHub Codespaces Usage

When running in GitHub Codespaces, open Port 8000 and use:
https://<codespace-name>-8000.app.github.dev/ask?q=Your%20question

Example:
https://silver-potato-xxxx-8000.app.github.dev/ask?q=What%20is%20trending%20in%20the%20news%20today

---
## 🛠 Common Issues & Fixes
### Internal Server Error
* Check logs:
docker compose logs ragbot
* Verify GNews API key
* Ensure Ollama is running
* Ensure model is pulled

### GNews API Errors
* Ensure query is URL-encoded
* Free plan has rate limits

### Ollama Not Responding
* Confirm container is running
* Verify correct model name
* Check /api/generate endpoint

---
## 🏁 Hackathon Checklist

 ✔ Live data ingestion
 
 ✔ Dynamic RAG pipeline
 
 ✔ Local LLM (no OpenAI)
 
 ✔ Dockerized deployment
 
 ✔ API-based interface
 
 ✔ Shareable demo URL

---
## 📌 Future Enhancements

* Add vector database
* Add streaming responses
* Add web UI
* Add article citations
* Add multi-language support

---
## 👨‍💻 Authors

This project was built as a **team hackathon project** by:

- Aditya  
- Soumyaranjan  
- Virinchy  

Dynamic RAG News Chatbot – Hackathon Project
