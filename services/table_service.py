from models.table import Table
from models.user import User
from fastapi import HTTPException

class TableService:
    @staticmethod
    async def get_all_available():
        return await Table.find(Table.is_booked == False).to_list()

    @staticmethod
    async def get_by_id(table_id: str) -> Table:
        table = await Table.get(table_id)
        if not table:
            raise HTTPException(status_code=404, detail="Table not found")
        return table

    @staticmethod
    async def book_table(table_id: str, user: User, persons: int = 1):
        table = await TableService.get_by_id(table_id)
        if table.is_booked:
            raise HTTPException(status_code=400, detail="Table already booked")
        table.client = str(user.id)
        table.is_booked = True
        table.persons = persons
        await table.save()
        return table

    @staticmethod
    async def cancel_booking(table_id: str, user: User):
        table = await TableService.get_by_id(table_id)
        if not table.is_booked:
            raise HTTPException(status_code=400, detail="Table is not booked")
        if table.client is None:
            raise HTTPException(status_code=400, detail="Table has no client")
        if table.client != str(user.id):
            raise HTTPException(status_code=403, detail="You can't cancel this booking")
        table.client = None
        table.is_booked = False
        table.persons = 0
        await table.save()
        return table

    @staticmethod
    async def change_booking(table_id: str, user: User, persons: int = 1):
        table = await TableService.get_by_id(table_id)
        if not table.is_booked:
            raise HTTPException(status_code=400, detail="Table is not booked")
        if table.client is None:
            raise HTTPException(status_code=400, detail="Table has no client")
        if table.client != str(user.id):
            raise HTTPException(status_code=403, detail="You can't change this booking")
        table.persons = persons
        await table.save()
        return table
