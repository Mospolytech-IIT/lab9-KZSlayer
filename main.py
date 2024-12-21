"""Модуль, запускающий FastAPI приложение и подключающий маршруты."""
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.requests import Request
import users
import posts
from models import Base
from database import engine
import os

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
Base.metadata.create_all(bind=engine)
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """Главная страница приложения."""
    return templates.TemplateResponse("index.html", {"request": request})
