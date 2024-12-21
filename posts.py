"""Модуль, содержащий маршруты для работы с постами."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud
import schemas
import database

router = APIRouter()

@router.post("/", response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db)):
    """Функция для создания нового Post."""
    return crud.create_post(db, post)

@router.get("/", response_model=list[schemas.PostOut])
def list_posts(db: Session = Depends(database.get_db)):
    """Функция для получения списка всех Post."""
    return crud.get_posts(db)
