from fastapi import APIRouter, HTTPException
from schemas.user import UserResponseSchema, UserSchema
from pydantic import ValidationError
from infrastructure.user import add_user, get_users, get_user_by_id

router = APIRouter()

@router.get("/users/", response_model=list[UserResponseSchema], tags=["Users"])
async def read_users() -> dict:
    users = await get_users()
    
    res: list[UserResponseSchema] = []
    for user in users:
        res.append(UserResponseSchema(id=user.id, name=user.name))
    
    return res

@router.post("/users/", response_model=None, tags=["Users"])
async def post_user(user: UserSchema) -> dict:
    await add_user(user.name)

@router.get("/users/{user_id}", response_model=UserResponseSchema, tags=["Users"])
async def get_user(user_id: int) -> dict:    
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
