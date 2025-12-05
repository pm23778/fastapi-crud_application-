# User service business logic
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.user_schema import UserCreate ,UserUpdate
from src.models.user import User
from fastapi import HTTPException, status

class UserService:

    @staticmethod
    async def create_user(db: AsyncSession, data: UserCreate):
        result = await db.execute(select(User).where(User.email == data.email))
        if result.scalar_one_or_none():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        user = User(name=data.name, email=data.email)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def get_users(db: AsyncSession):
        result = await db.execute(select(User))
        return result.scalars().all()

    @staticmethod
    async def get_user(db: AsyncSession, user_id: int):
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    @staticmethod
    async def update_user(db: AsyncSession, user_id: int, data: UserUpdate):
        user = await UserService.get_user(db, user_id)
        if data.name:
            user.name = data.name
        if data.email:
            user.email = data.email
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def delete_user(db: AsyncSession, user_id: int):
        user = await UserService.get_user(db, user_id)
        await db.delete(user)
        await db.commit()
        return user
