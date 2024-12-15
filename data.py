from typing import Optional

class User:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        
user_list = [
    User(id=1, name="hoge"),
    User(id=2, name="fuga"),
    User(id=3, name="piko"),
]

def get_user(user_id: int) -> User|None:
    for user in user_list:
        if user.id == user_id:
            return user
    return None
