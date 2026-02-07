from sqlalchemy import Text, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(200))
    raw_json: Mapped[str] = mapped_column(Text)

    markdown: Mapped[str] = mapped_column(Text)

    vacancy_text: Mapped[str] = mapped_column(Text, nullable=True)
    improved_version: Mapped[str] = mapped_column(Text, nullable=True)
