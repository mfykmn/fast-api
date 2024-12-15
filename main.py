from fastapi import FastAPI, HTTPException
from data import get_user, User

app = FastAPI()

@app.get("/")
async def get_hello():
    return {"message": "Hello World"}

@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    user: User|None = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.id, "user_name": user.name}

@app.get("/books/")
async def get_books(category: str|None = None) -> dict:
    return {"book_id": 1, "category": category}
