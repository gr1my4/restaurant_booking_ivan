from models.user import User
from pydantic import EmailStr
from fastapi import HTTPException
from schemas.user import UserCreate
from typing import Optional


class UserService:
    @staticmethod
    async def create_user(user_data: UserCreate) -> User:
        existing = await User.find_one(User.email == user_data.email)
        if existing:
            raise HTTPException(status_code=400, detail="User already exists")
        new_user = User(**user_data.model_dump(), is_active=True)
        await new_user.insert()
        return new_user

    @staticmethod
    async def get_by_email(email: EmailStr) -> Optional[User]:
        return await User.find_one(User.email == email)
