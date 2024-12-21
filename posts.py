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

@router.post("/bulk", response_model=list[schemas.PostOut])
def create_multiple_posts(posts: list[schemas.PostCreate], db: Session = Depends(database.get_db)):
    """Функция для добавления нескольких постов."""
    return crud.add_multiple_posts(db, posts)

@router.get("/all", response_model=list[schemas.PostOut])
def get_all_posts_with_users(db: Session = Depends(database.get_db)):
    """Функция для получения всех постов с пользователями."""
    return crud.get_all_posts_with_users(db)

@router.put("/{post_id}/content")
def update_post_content(post_id: int, new_content: str, db: Session = Depends(database.get_db)):
    """Функция для обновления content поста."""
    return crud.update_post_content(db, post_id, new_content)

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(database.get_db)):
    """Функция для удаления поста."""
    return crud.delete_post(db, post_id)
