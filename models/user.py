from sqlalchemy import Column, Integer, String
from infrastructure.db import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True} # sqliteでautoincrementしたい場合は必要

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
