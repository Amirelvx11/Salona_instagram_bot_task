import os
import httpx
from dotenv import load_dotenv
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL = os.getenv("HF_MODEL", "google/flan-t5-base")
MODEL_URL = os.getenv("MODEL_URL","https://api-inference.huggingface.co/models/google/flan-t5-base")

async def get_llm_replay(context: str, question:str):
    prompt = f"اطلاعات:\n{context}\nپرسش کاربر:\n{question}\nپاسخ بده فقط فارسی و با لحن طبیعی."
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    async with httpx.AsyncClient() as client:
        resp = await client.post(MODEL_URL, json={"inputs": prompt}, headers=headers, timeout=60)
        data = resp.json()
        return data[0]["generated_text"]
