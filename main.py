from fastapi import FastAPI
from routers.addresses import router as addesses_router
from routers.books import router as books_router
from routers.users import router as users_router

app = FastAPI()

app.include_router(addesses_router)
app.include_router(books_router)
app.include_router(users_router)
