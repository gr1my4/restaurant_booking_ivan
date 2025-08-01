from contextlib import asynccontextmanager
from fastapi import FastAPI
from db import init_db
from routers import user, table, auth_router

@asynccontextmanager
async def lifespan(_app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(table.router, prefix="/tables", tags=["Tables"])
app.include_router(auth_router.router, tags=["Auth"])
