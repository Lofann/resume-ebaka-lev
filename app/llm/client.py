import httpx
from app.config import settings


async def ask_llm(prompt: str) -> str:
    async with httpx.AsyncClient(timeout=180.0) as client:
        r = await client.post(
            settings.OLLAMA_URL,
            json={
                "model": settings.MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

    return r.json()["response"]
