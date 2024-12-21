"""Модуль, содержащий маршруты для работы с пользователями."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud
import schemas
import database

router = APIRouter()

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    """Функция для создания нового пользователя."""
    return crud.create_user(db, user)

@router.get("/", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(database.get_db)):
    """Функция для получения списка всех пользователей."""
    return crud.get_users(db)

@router.post("/bulk", response_model=list[schemas.UserOut])
def create_multiple_users(users: list[schemas.UserCreate], db: Session = Depends(database.get_db)):
    """Функция для добавления нескольких пользователей."""
    return crud.add_multiple_users(db, users)

@router.get("/all", response_model=list[schemas.UserOut])
def get_all_users(db: Session = Depends(database.get_db)):
    """Функция для получения всех пользователей."""
    return crud.get_all_users(db)

@router.put("/{user_id}/email")
def update_user_email(user_id: int, new_email: str, db: Session = Depends(database.get_db)):
    """Функция для обновления email пользователя."""
    return crud.update_user_email(db, user_id, new_email)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    """Функция для удаления пользователя и его постов."""
    return crud.delete_user_and_posts(db, user_id)
