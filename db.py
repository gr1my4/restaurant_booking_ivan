import os
from dotenv import load_dotenv
from typing import cast, Any
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.user import User
from models.table import Table

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")

async def init_db():
    client = AsyncIOMotorClient(MONGO_URL)
    db = cast(Any, client["Ivan_TestCase"])
    await init_beanie(database=db, document_models=[User, Table])
