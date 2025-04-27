from fastapi import FastAPI
from src.blogs.routes import blog_router

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

app.include_router(blog_router, prefix="/blogs", tags=["blogs"])