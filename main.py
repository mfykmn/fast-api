from fastapi import FastAPI, HTTPException
from data import get_user, User
from pydantic import ValidationError

app = FastAPI()

@app.get("/")
async def get_hello():
    return {"message": "Hello World"}

@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    try:
        user: User|None = get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {"user_id": user.id, "user_name": user.name}
    except ValidationError as e: # 実際は起きないpost作ったらそこに移す
        raise HTTPException(status_code=400, detail="Validation error")

@app.get("/books/")
async def get_books(category: str|None = None) -> dict:
    return {"book_id": 1, "category": category}
