from fastapi import FastAPI
from pydantic import BaseModel

from .rag import rag_pipeline

app = FastAPI(title="Salona Bot Task", version="1.0")

class DMRequest(BaseModel):
    sender_id: str
    message_id: str
    text: str

@app.post("/simulate_dm")
async def simulate_dm(req: DMRequest):
    """ Receive a simulated DM message from user and generate AI response. """
    reply = await rag_pipeline(req.text)
    return {"reply": reply}
