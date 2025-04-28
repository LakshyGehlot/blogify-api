from fastapi import APIRouter, HTTPException, Depends
from .schema import Blog, CreateBlog, UpdateBlog
from .services import BlogService
from typing import List
from src.db.model import BlogModel
from src.db.session import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession

blog_router = APIRouter()

blog_service = BlogService()

@blog_router.get("/", response_model=List[Blog])
async def get_blogs(session: AsyncSession = Depends(get_session)):
    return await blog_service.get_all_blogs(session)

@blog_router.get("/{blog_id}", response_model=Blog)
async def get_blog(blog_id: str, session: AsyncSession = Depends(get_session)):
    blog = await blog_service.get_blog_by_id(blog_id, session)
    if blog:
        return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@blog_router.post("/", response_model=Blog)
async def create_blog(blog: CreateBlog, session: AsyncSession = Depends(get_session)):
    return await blog_service.create_blog(blog, session)

@blog_router.put("/{blog_id}", response_model=Blog)
async def update_blog(blog_id: str, update_blog: UpdateBlog, session: AsyncSession = Depends(get_session)):
    blog = await blog_service.update_blog(blog_id, update_blog, session)
    if blog:
        return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@blog_router.delete("/{blog_id}", response_model=Blog)
async def delete_blog(blog_id: str, session: AsyncSession = Depends(get_session)):
    blog = await blog_service.delete_blog(blog_id, session)
    if blog:
        return blog
    raise HTTPException(status_code=404, detail="Blog not found")
