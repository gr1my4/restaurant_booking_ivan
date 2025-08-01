from beanie import Document
from typing import Optional
from uuid import uuid4
from datetime import time
from pydantic import Field

class Table(Document):
    id: str = Field(default_factory=lambda: str(uuid4()))
    max_persons: int
    booking_time: Optional[time] = None
    persons: int = 0
    is_booked: bool = False
    client: Optional[str] = None

    class Settings:
        name = "tables"

