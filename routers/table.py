from fastapi import APIRouter, Depends, Query
from schemas.table import TableOut
from models.user import User
from services.table_service import TableService
from auth.security import get_current_user

router = APIRouter()

@router.get("/available", response_model=list[TableOut])
async def get_available_tables():
    return await TableService.get_all_available()

@router.post("/book/{table_id}", response_model=TableOut)
async def book_table(
    table_id: str,
    persons: int = Query(1, ge=1, description="Количество человек"),
    user: User = Depends(get_current_user)
):
    return await TableService.book_table(table_id, user, persons)

@router.post("/cancel/{table_id}", response_model=TableOut)
async def cancel_table(
    table_id: str,
    user: User = Depends(get_current_user)
):
    return await TableService.cancel_booking(table_id, user)

@router.post("/change/{table_id}", response_model=TableOut)
async def change_table_booking(
    table_id: str,
    persons: int = Query(1, ge=1, description="Новое количество человек"),
    user: User = Depends(get_current_user)
):
    return await TableService.change_booking(table_id, user, persons)


