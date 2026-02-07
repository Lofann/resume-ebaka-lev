from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False
)

SessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# Dependency для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

