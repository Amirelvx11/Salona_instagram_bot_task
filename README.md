# Salona Bot — Instagram DM Simulator (FastAPI + RAG + OpenRouter Free LLM)

## 📘 Overview
**Salona Bot** is a technical task project that implements a simulated Instagram DM assistant using **FastAPI**, **SQLite**, and **Retrieval‑Augmented Generation (RAG)** combined with a **Free LLM on OpenRouter**.  
The bot retrieves product information from a local database and generates intelligent, context‑aware replies in **Persian**.

---

## 🧠 Architecture

| Module | Description |
|--------|--------------|
| `main.py` | Application entry‑point. Launches FastAPI app. |
| `app/api.py` | Defines REST endpoints, including `/simulate_dm`. |
| `app/db.py` | Handles SQLite connections and product search queries. |
| `app/rag.py` | Implements retrieval logic and prompt composition for RAG pipeline. |
| `app/llm_free.py` | Connects to free models from OpenRouter with fallback mechanism. |
| `scripts/populate_db.py` | Initializes the database with 100 diverse product records (phones, laptops, headphones, cameras). |

---

## 💾 Requirements

Python ≥ 3.10  
Install dependencies:
```bash
pip install -r requirements.txt

content_copy
text
fastapi
uvicorn
httpx
python-dotenv
SQLite is included in Python’s standard library (no additional dependency required).

🔐 How to Configure the Free API Key
To enable the LLM connection, create an .env file in the project root directory and include your free OpenRouter API key:


content_copy
dotenv
OPENROUTER_API_KEY="YOUR_FREE_API_KEY_HERE"
BASE_URL="https://openrouter.ai/api/v1"
If you use multiple free models, refer to the fallback list inside app/llm_free.py:


content_copy
python

note_add
ویرایش با Canvas
MODEL_FALLBACKS = [
"z-ai/glm-4.5-air:free",
"openrouter/andromeda-alpha",
"liquid/lfm2-8b-a1b"
]
➡️ Important:

Never commit .env or any real keys to GitHub. Only .env.example should be pushed and contain placeholders for configuration.

Example of .env.example:


content_copy
dotenv
OPENROUTER_API_KEY="YOUR_API_KEY_HERE"
OPENROUTER_URL="https://openrouter.ai/api/v1"
🚀 Running the Server
Populate the SQLite database:

content_copy
bash

note_add
ویرایش با Canvas
   python scripts/populate_db.py
Launch the server:

content_copy
bash

note_add
ویرایش با Canvas
   uvicorn main:app --reload --port 8000
Server will start at: http://127.0.0.1:8000

🔎 Endpoint Specification — /simulate_dm
This endpoint simulates a user Direct Message (DM) and returns an intelligent, dynamic reply based on product data and LLM reasoning.

▶️ Example request (JSON)

content_copy
json

note_add
ویرایش با Canvas
{
  "sender_id": "user123",
  "message_id": "m-001",
  "text": "قیمت گوشی سامسونگ Galaxy A54 چقدره؟"
}
💬 Example response (JSON)

content_copy
json

note_add
ویرایش با Canvas
{
  "reply": "گوشی سامسونگ Galaxy A54 با قیمت حدود 22,000,000 تومان موجود است."
}
🧠 How It Works (RAG Flow)
The system parses the incoming user message.
It searches for relevant product info in the SQLite database (case-insensitive).
Retrieved data is embedded into a contextual prompt.
The prompt is sent to the free model through the OpenRouter API.
The model returns a fluent Persian response enriched with factual product details.
🧪 Testing with Curl
Use the following command to test locally:


content_copy
bash

note_add
ویرایش با Canvas
curl -X POST "http://127.0.0.1:8000/simulate_dm" \
-H "Content-Type: application/json" \
-d '{"sender_id": "user001", "message_id": "m-002", "text": "قیمت موس Logitech MX Master 3S رو می‌خوام"}'
Expected output:


content_copy
json

note_add
ویرایش با Canvas
{
  "reply": "موس Logitech MX Master 3S با قیمت حدود 7,200,000 تومان و سنسور دقیق عرضه می‌شود."
}