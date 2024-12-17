from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    name: str = Field(..., description="ユーザネーム", example="田中")

class UserResponseSchema(UserSchema):
    id: int
