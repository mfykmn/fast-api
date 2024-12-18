from fastapi import FastAPI
from routers.addresses import router as addesses_router
from routers.books import router as books_router
from routers.users import router as users_router
from infrastructure.db import init_db

app = FastAPI()

@app.on_event("startup") # TODO: 非推奨
async def start_db():
    await init_db()

app.include_router(addesses_router)
app.include_router(books_router)
app.include_router(users_router)
