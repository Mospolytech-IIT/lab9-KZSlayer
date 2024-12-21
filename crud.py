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

def add_multiple_users(db: Session, users: list[schemas.UserCreate]):
    """Функция для добавления нескольких пользователей."""
    db_users = [models.User(username=user.username, email=user.email, password=user.password) for user in users]
    db.add_all(db_users)
    db.commit()
    for db_user in db_users:
        db.refresh(db_user)
    return db_users

def get_all_users(db: Session):
    """Функция для извлечения всех пользователей."""
    return db.query(models.User).all()

def get_all_posts_with_users(db: Session):
    """Функция для извлечения всех постов с информацией о пользователях."""
    return db.query(models.Post).join(models.User).all()

def get_posts_by_user(db: Session, user_id: int):
    """Функция для извлечения постов конкретного пользователя."""
    return db.query(models.Post).filter(models.Post.user_id == user_id).all()

def update_user_email(db: Session, user_id: int, new_email: str):
    """Функция для обновления email у пользователя."""
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.email = new_email
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user_and_posts(db: Session, user_id: int):
    """Функция для удаления пользователя и всех его постов."""
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def get_user_by_id(db: Session, user_id: int):
    """Функция для получения пользователя по ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db: Session, user_id: int, new_email: str):
    """Функция для обновления email пользователя."""
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.email = new_email
        db.commit()
        db.refresh(user)
        return user
    return None
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

def add_multiple_posts(db: Session, posts: list[schemas.PostCreate]):
    """Функция для добавления нескольких постов."""
    db_posts = [models.Post(title=post.title, content=post.content, user_id=post.user_id) for post in posts]
    db.add_all(db_posts)
    db.commit()
    for db_post in db_posts:
        db.refresh(db_post)
    return db_posts

def update_post_content(db: Session, post_id: int, new_content: str):
    """Функция для обновления content у поста."""
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db_post.content = new_content
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    """Функция для удаления поста."""
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post

def get_post_by_id(db: Session, post_id: int):
    """Функция для получения поста по ID."""
    return db.query(models.Post).filter(models.Post.id == post_id).first()
