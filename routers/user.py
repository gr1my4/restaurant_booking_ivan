from fastapi import APIRouter
from models.user import User
from schemas.user import UserOut

router = APIRouter(
    tags=["Users"]
)

@router.get("/", response_model=list[UserOut])
async def get_users():
    users = await User.find_all().to_list()
    return users
