from fastapi import FastAPI, HTTPException
from data import get_user, User
from pydantic import ValidationError
from book_schemas import BookResponseSchema, BookSchema

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

books: list[BookResponseSchema] = [
    BookResponseSchema(id=1, title="hoge", category="comics"),
    BookResponseSchema(id=2, title="fuga", category="comics"),
    BookResponseSchema(id=3, title="pika", category="magazine"),
    BookResponseSchema(id=4, title="chu", category="magazine"),
    
]

@app.get("/books/")
async def get_books(category: str|None = None) -> dict:
    return {"book_id": 1, "category": category}

@app.post("/books/", response_model=BookResponseSchema)
async def post_books(book: BookSchema):
    '''書籍登録
    '''
    new_book_id = max([book.id for book in books], default=0) + 1
    new_book = BookResponseSchema(id=new_book_id, **book.model_dump())
    books.append(new_book)
    return new_book
