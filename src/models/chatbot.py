import uuid

from sqlmodel import Field, SQLModel

from typing import Optional


class Chatbot(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    key: str = Field(min_length=1, max_length=256, default=None, unique=True, index=True)
    model: str = Field(min_length=1, max_length=1024, default=None)
    system_prompt: str = Field(min_length=1, max_length=65536, default=None)
