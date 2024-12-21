"""Модуль с функциями для работы с базой данных (CRUD)."""
from sqlalchemy.orm import Session
import models
import schemas

def create_user(db: Session, user: schemas.UserCreate):
    """Функция для создания нового пользователя."""
    db_user = models.User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    """Функция для получения списка всех пользователей."""
    return db.query(models.User).all()

# CRUD для постов
def create_post(db: Session, post: schemas.PostCreate):
    """Функция для создания нового Post."""
    db_post = models.Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session):
    """Функция для получения списка всех Post."""
    return db.query(models.Post).all()
