from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid
from sqlalchemy import func
from typing import List

class BlogModel(SQLModel, table=True):
    __tablename__ = 'blog'
    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
            pg.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid.uuid4
        )
    )
    title: str
    content: str
    published: bool = Field(default=False)
    published_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, server_default=func.now()))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, server_default=func.now(), onupdate=func.now()))
    author: str
    tags: List[str] = Field(sa_column=Column(pg.ARRAY(pg.VARCHAR)))