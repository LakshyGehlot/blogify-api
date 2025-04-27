from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class Blog(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    published: bool = True
    tags: List[str] = []
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    createdBy: str

class BlogCreate(BaseModel):
    title: str
    content: str
    published: bool = True
    tags: List[str] = []
    createdBy: str
