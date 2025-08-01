from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import time, datetime
from constants import TZ

class TableCreate(BaseModel):
    max_persons: int
    booking_time: Optional[time] = None

class TableOut(BaseModel):
    id: str
    max_persons: int
    booking_time: Optional[time]
    persons: int
    is_booked: bool

class TableBookSchema(BaseModel):
    persons: int
    booking_time: time

    @field_validator("booking_time")
    def check_booking_time(cls, value: time) -> time:
        now = datetime.now(tz=TZ).time()
        if now > time(22, 0):
            raise ValueError("Booking is only allowed before 22:00")
        return value

