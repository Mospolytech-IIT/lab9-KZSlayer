"""Модуль, запускающий FastAPI приложение и подключающий маршруты."""
from fastapi import FastAPI
import users
import posts
from models import Base
from database import engine
app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
Base.metadata.create_all(bind=engine)
@app.get("/")
def read_root():
    """Главная страница приложения."""
    return {"message": "Добро пожаловать в приложение FastAPI"}
