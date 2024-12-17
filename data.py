from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., description="ユーザーの識別子", example=1)
    name: str = Field(..., description="ユーザネーム", example="田中")
        
user_list = [
    User(**{"id": 1, "name":"hoge"}),
    User(**{"id": 2, "name":"fuga"}),
    
    User(id = 3, name="pika"),
]

def get_user(user_id: int) -> User|None:
    for user in user_list:
        if user.id == user_id:
            return user
    return None
