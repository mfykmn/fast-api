from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from routers.addresses import router as addesses_router
from routers.books import router as books_router
from routers.users import router as users_router
from infrastructure.db import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(ValidationError)
async def validation_exception_handler(exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors(),
            "body": exc.model,
        }
    )

@app.on_event("startup") # TODO: 非推奨
async def start_db():
    await init_db()

app.include_router(addesses_router)
app.include_router(books_router)
app.include_router(users_router)
