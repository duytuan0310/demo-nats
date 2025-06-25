import uuid
from collections.abc import Generator
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine
from typing import Annotated
from fastapi import Depends
from app.core.setting import settings

engine = create_engine(
    settings.DATABASE_URI,
    echo=True,
)
def get_db() -> Generator[Session, None, None]:
    """Get a database session."""
    with Session(engine) as session:
        yield session
Database = Annotated[Session, Depends(get_db)]

class BaseModel(SQLModel):
    """Base database model."""
    id : uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: str = Field(default_factory=datetime.now)
    updated_at: str = Field(default_factory=datetime.now)