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
