import os
import httpx
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_URL = os.getenv("OPENROUTER_URL", "https://openrouter.ai/api/v1/chat/completions")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL_FALLBACKS = [
    "z-ai/glm-4.5-air:free",
    "openrouter/andromeda-alpha",
    "liquid/lfm2-8b-a1b"
]

async def query_openrouter(prompt: str) -> str:
    """ Query the OpenRouter API using available free models with fallback sequence. """
    for model in MODEL_FALLBACKS:
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        }
        async with httpx.AsyncClient(timeout=80.0) as client:
            r = await client.post(
                OPENROUTER_URL,
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                },
                json=payload,
            )

        data = r.json()
        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        elif data.get("error", {}).get("code") in (400, 402):
            continue
    return "در حال حاضر مدل رایگان در دسترس نیست."
