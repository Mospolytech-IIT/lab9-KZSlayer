"""Модуль, содержащий маршруты для работы с пользователями."""
from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.requests import Request
import crud
import schemas
import database
import os

router = APIRouter()

# Настройка шаблонов
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

@router.get("/create", response_class=HTMLResponse)
def create_user_form(request: Request):
    """Страница для создания нового пользователя."""
    return templates.TemplateResponse("create_user.html", {"request": request})

@router.post("/create", response_class=RedirectResponse)
def create_user(username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(database.get_db)):
    """Функция для создания нового пользователя."""
    user = schemas.UserCreate(username=username, email=email, password=password)
    crud.create_user(db, user)
    return RedirectResponse(url="/users/", status_code=303)

@router.get("/", response_class=HTMLResponse)
def list_users(request: Request, db: Session = Depends(database.get_db)):
    """Страница для отображения всех пользователей."""
    users = crud.get_users(db)
    return templates.TemplateResponse("list_users.html", {"request": request, "users": users})

@router.get("/edit/{user_id}", response_class=HTMLResponse)
def edit_user_form(request: Request, user_id: int, db: Session = Depends(database.get_db)):
    """Страница для редактирования пользователя."""
    user = crud.get_user_by_id(db, user_id)
    return templates.TemplateResponse("edit_user.html", {"request": request, "user": user})

@router.post("/edit/{user_id}", response_class=RedirectResponse)
def edit_user(user_id: int, username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(database.get_db)):
    """Функция для обновления данных пользователя."""
    user = schemas.UserCreate(username=username, email=email, password=password)
    crud.update_user(db, user_id, user)
    return RedirectResponse(url="/users/", status_code=303)

@router.get("/delete/{user_id}", response_class=RedirectResponse)
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    """Функция для удаления пользователя и его постов."""
    crud.delete_user_and_posts(db, user_id)
    return RedirectResponse(url="/users/", status_code=303)
