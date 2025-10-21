from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DMRequest(BaseModel):
    sender_id: str
    message_id: str
    text: str

@app.post("/simulate_dm")
async def simulate_dm(request: DMRequest):
    return {
        "reply": f"✅ پیام شما با موفقیت دریافت شد، {request.sender_id}. "
                f"متن ارسالی: «{request.text}». فعلاً همه‌چیز برای تست اولیه کاملاً سالم است."
    }