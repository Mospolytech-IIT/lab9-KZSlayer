"""Модуль, содержащий схемы для валидации данных."""
from pydantic import BaseModel

class UserBase(BaseModel):
    """Схема, представляющая базовую информацию о пользователе."""
    username: str
    email: str

class UserCreate(UserBase):
    """Схема, представляющая информацию для создания нового пользователя."""
    password: str

class UserOut(UserBase):
    """Схема, представляющая пользователя с его идентификатором."""
    id: int
    class Config:
        """Конфигурация для работы с ORM-моделями."""
        orm_mode = True

class PostBase(BaseModel):
    """Схема, представляющая базовую информацию о Post."""
    title: str
    content: str

class PostCreate(PostBase):
    """Схема, представляющая данные для создания нового Post."""
    user_id: int

class PostOut(PostBase):
    """Схема, представляющая Post с его данными и автором."""
    id: int
    user: UserOut
    class Config:
        """Конфигурация для работы с ORM-моделями."""
        orm_mode = True
