from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

tags_metadata = [
    {
        "name": "blogs",
        "description": "Operations with blogs"
    }
]

app = FastAPI(
    title="Blogs API",
    description="A simple API for managing blogs",
    version="0.01",
    tags_metadata=tags_metadata
)

class Blog(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    published: bool = True
    tags: List[str] = []
    created_at: datetime = datetime.now()
    createdBy: str

class BlogCreate(BaseModel):
    title: str
    content: str
    published: bool = True
    tags: List[str] = []
    createdBy: str

Blogs: List[Blog] = []
id_counter: int = 1

@app.get("/blogs", response_model=List[Blog], tags=["blogs"])
def get_blogs():
    return Blogs

@app.get("/blogs/{blog_id}", response_model=Blog, tags=["blogs"])
def get_blog(blog_id: int):
    for blog in Blogs:
        if blog.id == blog_id:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@app.post("/blogs", response_model=Blog, tags=["blogs"])
def create_blog(blog: BlogCreate):
    global id_counter
    new_blog = Blog(id=id_counter, **blog.dict())
    Blogs.append(new_blog)
    id_counter += 1
    return new_blog

@app.put("/blogs/{blog_id}", response_model=Blog, tags=["blogs"])
def update_blog(blog_id: int, update_blog: BlogCreate):
    for i, blog in enumerate(Blogs):
        if blog.id == blog_id:
            for key, value in update_blog.model_dump().items():
                setattr(blog, key, value)
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@app.delete("/blogs/{blog_id}", response_model=Blog, tags=["blogs"])
def delete_blog(blog_id: int):
    for i, blog in enumerate(Blogs):
        if blog.id == blog_id:
            deleted_blog = Blogs.pop(i)
            return deleted_blog
    raise HTTPException(status_code=404, detail="Blog not found")
