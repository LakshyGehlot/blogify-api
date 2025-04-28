from fastapi import FastAPI
from src.blogs.routes import blog_router
from src.db.session import init_db, engine
from contextlib import asynccontextmanager

tags_metadata = [
    {
        "name": "blogs",
        "description": "Operations with blogs"
    }
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await engine.dispose()

app = FastAPI(
    title="Blogs API",
    description="A simple API for managing blogs",
    version="0.01",
    tags_metadata=tags_metadata,
    lifespan=lifespan
)

app.include_router(blog_router, prefix="/blogs", tags=["blogs"])