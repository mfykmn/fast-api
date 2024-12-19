from fastapi import APIRouter, HTTPException, Depends
from schemas.user import UserResponseSchema, UserSchema
from pydantic import ValidationError
from infrastructure.user import add_user, get_users, get_user_by_id

router = APIRouter(tags=["Users"], prefix="/users")

@router.get("/", response_model=list[UserResponseSchema])
async def read_users(users = Depends(get_users)) -> dict:    
    res: list[UserResponseSchema] = []
    for user in users:
        res.append(UserResponseSchema(id=user.id, name=user.name))
    
    return res

@router.post("/users/", response_model=None, tags=["Users"])
async def post_user(user: UserSchema) -> dict:
    await add_user(user.name)

@router.get("/{user_id}", response_model=UserResponseSchema)
async def get_user(user_id: int) -> dict:
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
