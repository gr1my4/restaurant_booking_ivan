from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from models.user import User
from auth.jwt import create_access_token
from datetime import timedelta
from constants import JWT_EXP_HOURS
from auth.security import hash_password, verify_password
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

class UserRegister(BaseModel):
    email: str
    password: str
    name: str
    phone: str

@router.post("/register")
async def register_user(user: UserRegister):
    existing = await User.find_one(User.email == user.email)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_pw = hash_password(user.password)
    new_user = User(
        email=user.email,
        password=hashed_pw,
        name=user.name,
        phone=user.phone,
        is_active=True
    )
    await new_user.insert()
    token = create_access_token({"sub": str(new_user.id)}, expires_delta=timedelta(hours=JWT_EXP_HOURS))
    return {"access_token": token, "token_type": "bearer"}

@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = await User.find_one(User.email == form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": str(db_user.id)}, expires_delta=timedelta(hours=JWT_EXP_HOURS))
    return {"access_token": token, "token_type": "bearer"}


