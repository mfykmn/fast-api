from fastapi import APIRouter, HTTPException
from schemas.user import UserResponseSchema
from pydantic import ValidationError
from infrastructure.user import add_user, get_users

router = APIRouter()

user_list = [
    UserResponseSchema(**{"id": 1, "name":"hoge"}),
    UserResponseSchema(**{"id": 2, "name":"fuga"}),
    UserResponseSchema(**{"id": 3, "name":"pika"}),
]

@router.get("/users/{user_id}", response_model=list[UserResponseSchema], tags=["Users"])
async def read_user(user_id: int) -> dict:
    # TODO: 動作確認用
    #await add_user("hoge")
    #await add_user("fuga")
    #users = await get_users()
    #print(users)
    # TODO: 
    
    try:
        user: UserResponseSchema|None = get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except ValidationError as e: # 実際は起きないpost作ったらそこに移す
        raise HTTPException(status_code=400, detail="Validation error")

def get_user(user_id: int) -> UserResponseSchema|None:
    for user in user_list:
        if user.id == user_id:
            return user
    return None
