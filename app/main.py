from fastapi import FastAPI
from pydantic import BaseModel
from .llm import get_llm_replay
from .rag import retrieve_context

app = FastAPI()

class DMRequest(BaseModel):
    sender_id: str
    message_id: str
    text: str

@app.post("/simulate_dm")
async def simulate_dm(request: DMRequest):
    context = retrieve_context(request.text)
    reply_text = await get_llm_replay(context, request.text)

    return {"reply": reply_text}

