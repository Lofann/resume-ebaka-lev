import os


class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://postgres:postgres@db:5432/resume_db"
    )

    OLLAMA_URL: str = os.getenv(
        "OLLAMA_URL",
        "http://0.0.0.0:11434/api/generate"
    )

    MODEL: str = os.getenv("MODEL", "gemma3:12b")


settings = Settings()
