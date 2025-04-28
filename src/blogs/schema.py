from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
import uuid

class Blog(BaseModel):
    uid: uuid.UUID
    title: str
    content: str
    published: bool = True
    tags: List[str] = []
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    author: str

    class Config:
        orm_mode = True

class CreateBlog(BaseModel):
    title: str
    content: str
    published: bool = True
    tags: List[str] = []
    author: str

    class Config:
        orm_mode = True

class UpdateBlog(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None
    tags: Optional[List[str]] = None
    author: Optional[str] = None

    class Config:
        orm_mode = True
