from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select
from .schema import CreateUser, UpdateUser
from src.db.model import UserModel
from src.utils import hash_password

class AuthServices:
    async def get_user_by_email(self, email: str, session: AsyncSession):
        statement = select(UserModel).where(UserModel.email == email)
        result = await session.execute(statement)
        user = result.scalar_one_or_none()
        return user
    
    async def get_user_by_id(self, user_id: str, session: AsyncSession):
        statement = select(UserModel).where(UserModel.uid == user_id)
        result = await session.execute(statement)
        return result.scalar_one_or_none()

    
    async def user_exists(self, email: str, session: AsyncSession):
        user = await self.get_user_by_email(email, session)
        return True if user is not None else False
    
    async def create_user(self, user_data: CreateUser, session: AsyncSession):
        user = UserModel(**user_data.model_dump())
        user.password_hash = hash_password(user_data.password)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
    
    async def update_user(self, user_id: str, user_data: UpdateUser, session: AsyncSession):
        user = await self.get_user_by_id(user_id, session)
        if user is None:
            return None
        
        for key, value in user_data.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(user, key, value)
        if user_data.password is not None:
            user.password_hash = hash_password(user_data.password)
        await session.commit()
        await session.refresh(user)
        return user
    