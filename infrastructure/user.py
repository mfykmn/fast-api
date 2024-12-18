from models.user import User
from infrastructure.db import async_session
from sqlalchemy import select

async def add_user(name: str):
    async with async_session() as session:
        async with session.begin():
            user = User(name=name)
            session.add(user)
            
async def get_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users
