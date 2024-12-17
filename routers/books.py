from fastapi import APIRouter, HTTPException
from schemas.book import BookResponseSchema, BookSchema

router = APIRouter()

books: list[BookResponseSchema] = [
    BookResponseSchema(id=1, title="hoge", category="comics"),
    BookResponseSchema(id=2, title="fuga", category="comics"),
    BookResponseSchema(id=3, title="pika", category="magazine"),
    BookResponseSchema(id=4, title="chu", category="magazine"),   
]

@router.get("/books/", response_model=list[BookResponseSchema], tags=["Books"])
async def get_books():
    '''書籍一覧取得
    '''
    return books

@router.get("/books/{book_id}", response_model=BookResponseSchema, tags=["Books"])
async def get_book(book_id: int):
    '''書籍取得
    '''
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found") 

@router.post("/books/", response_model=BookResponseSchema, tags=["Books"])
async def post_book(book: BookSchema):
    '''書籍登録
    '''
    new_book_id = max([book.id for book in books], default=0) + 1
    new_book = BookResponseSchema(id=new_book_id, **book.model_dump())
    books.append(new_book)
    return new_book

@router.put("/books/{book_id}", response_model=BookResponseSchema, tags=["Books"])
async def put_book(book_id: int, book: BookSchema):
    '''書籍更新
    '''
    for index, existing_book in enumerate(books):
        if existing_book.id == book_id:
            updated_book = BookResponseSchema(id=book_id, **book.model_dump())
            books[index] = updated_book
            return updated_book
            
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/books/{book_id}", response_model=BookResponseSchema, tags=["Books"])
async def delete_book(book_id: int):
    '''書籍削除
    '''
    for index, book in enumerate(books):
        if book.id == book_id:
            book.pop(index)
            return book
    raise HTTPException(status_code=404, detail="Book not found")
