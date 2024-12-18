import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

base_dir = os.path.dirname(__file__)
DATABASE_URL = 'sqlite+aiosqlite:///' + os.path.join(base_dir, 'example.sqlite')
engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

Base = declarative_base()

async def init_db():
    print("データベースの初期化を開始します。")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        print("既存のテーブルを削除しました。")
        await conn.run_sync(Base.metadata.create_all)
        print("新しいテーブルを作成しました。")
