from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    name: str
    phone: str

class UserOut(BaseModel):
    id: str
    email: str
    name: str
    phone: str
    is_active: bool

    class Config:
        from_attributes = True
