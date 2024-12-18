from sqlalchemy import Column, Integer, String
from infrastructure.db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
