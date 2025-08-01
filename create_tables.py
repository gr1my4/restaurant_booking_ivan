import asyncio
from models.table import Table
from models.user import User
from db import init_db
from auth.security import hash_password

async def seed_tables():
    await init_db()

    existing_tables = await Table.find_all().to_list()
    if existing_tables:
        print(f" {len(existing_tables)} tables already exist. Skipping creation.")
    else:
        fixtures = [2] * 7 + [3] * 6 + [6] * 3
        for max_persons in fixtures:
            table = Table(max_persons=max_persons, persons=0, is_booked=False)
            await table.insert()
        print("Tables created successfully.")

    await create_test_user()


async def create_test_user():
    email = "testuser@mail.com"
    existing = await User.find_one(User.email == email)
    if existing:
        print("Test user already exists.")
        return
    hashed_pw = hash_password("123456")
    user = User(
        email=email,
        password=hashed_pw,
        name="Test User",
        phone="7771234567",
        is_active=True
    )
    await user.insert()
    print("Test user created: testuser@mail.com / 123456")


if __name__ == "__main__":
    asyncio.run(seed_tables())

