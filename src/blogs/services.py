from src.db.model import BlogModel
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from .schema import CreateBlog, UpdateBlog
from datetime import datetime

class BlogService:

    async def get_all_blogs(self, session: AsyncSession):
        statement = select(BlogModel).order_by(desc(BlogModel.published_at))
        result = await session.execute(statement)
        return result.scalars().all()
    
    async def get_blog_by_id(self, blog_id: str, session: AsyncSession):
        statement = select(BlogModel).where(BlogModel.uid == blog_id)
        result = await session.execute(statement)
        return result.scalars().first()
    
    async def create_blog(self, blog: CreateBlog, session: AsyncSession):
        new_blog = BlogModel(**blog.model_dump())
        session.add(new_blog)
        await session.commit()
        await session.refresh(new_blog)
        return new_blog
    
    async def update_blog(self, blog_id: str, blog_data: UpdateBlog, session: AsyncSession):
        blog_to_update = await self.get_blog_by_id(blog_id, session)
        if blog_to_update is not None:
            for k, v in blog_data.model_dump().items():
                if v is not None:
                    setattr(blog_to_update, k, v)
            blog_to_update.updated_at = datetime.now()
            await session.commit()
            await session.refresh(blog_to_update)
            return blog_to_update
        else:
            return None
        
    async def delete_blog(self, blog_id: str, session: AsyncSession):
        blog_to_delete = await self.get_blog_by_id(blog_id, session)
        if blog_to_delete is not None:
            await session.delete(blog_to_delete)
            await session.commit()
            return blog_to_delete
        else:
            return None