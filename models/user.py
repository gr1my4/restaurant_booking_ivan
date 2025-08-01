from beanie import Document
from pydantic import Field
from uuid import uuid4

class User(Document):
    id: str = Field(default_factory=lambda: str(uuid4()))
    email: str
    password: str
    name: str
    phone: str
    is_active: bool = False

    class Settings:
        name = "users"
