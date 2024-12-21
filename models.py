"""Модуль, содержащий модели для базы данных."""
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    """Класс, представляющий пользователя."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")

class Post(Base):
    """Класс, представляющий Post."""
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="posts")
