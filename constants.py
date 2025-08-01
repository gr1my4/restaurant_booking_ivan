from datetime import timedelta, timezone
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_URL: str
    JWT_SECRET: str = "your-secret-key"
    JWT_ALGO: str = "HS256"
    JWT_EXP_HOURS: int = 1
    TZ_SHIFT: float = 5.0

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

sets = Settings()

JWT_SECRET = sets.JWT_SECRET
JWT_ALGO = sets.JWT_ALGO
JWT_EXP_HOURS = sets.JWT_EXP_HOURS

DEADLINE_HOURS = 1
TZ = timezone(timedelta(hours=sets.TZ_SHIFT))

