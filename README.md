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
