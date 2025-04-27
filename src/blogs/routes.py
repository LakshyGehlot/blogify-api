from fastapi import APIRouter, HTTPException
from .schema import Blog, BlogCreate
from typing import List
from datetime import datetime

blog_router = APIRouter()

Blogs: List[Blog] = []
id_counter: int = 1

@blog_router.get("/", response_model=List[Blog])
def get_blogs():
    return Blogs

@blog_router.get("/{blog_id}", response_model=Blog)
def get_blog(blog_id: int):
    for blog in Blogs:
        if blog.id == blog_id:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@blog_router.post("/", response_model=Blog)
def create_blog(blog: BlogCreate):
    global id_counter
    new_blog = Blog(id=id_counter, **blog.model_dump())
    Blogs.append(new_blog)
    id_counter += 1
    return new_blog

@blog_router.put("/{blog_id}", response_model=Blog)
def update_blog(blog_id: int, update_blog: BlogCreate):
    for i, blog in enumerate(Blogs):
        if blog.id == blog_id:
            for key, value in update_blog.model_dump().items():
                setattr(blog, key, value)
            blog.updated_at = datetime.now()
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@blog_router.delete("/{blog_id}", response_model=Blog)
def delete_blog(blog_id: int):
    for i, blog in enumerate(Blogs):
        if blog.id == blog_id:
            deleted_blog = Blogs.pop(i)
            return deleted_blog
    raise HTTPException(status_code=404, detail="Blog not found")
