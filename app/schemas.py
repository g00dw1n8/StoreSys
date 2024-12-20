# schemas.py
from pydantic import BaseModel
from pydantic import BaseModel, EmailStr
from pydantic.types import constr
from typing import Optional


class UserCreate(BaseModel):
    # Минимум 3, максимум 50 символов для имени
    name: constr(min_length=3, max_length=60)
    email: EmailStr  # Email должен быть валидным
    # Ограничение на длину пароля (например, минимум 8 символов)
    password: constr(min_length=6)

    class Config:
        orm_mode = True  # Для работы с ORM (если используется SQLAlchemy)


class User(BaseModel):
    id: int
    name: str
    email: EmailStr


class Login(BaseModel):  # Модель для аутентификации пользователя (логин)
    email: EmailStr
    password: str


# Модель для ответа с токеном
class Token(BaseModel):
    access_token: str
    token_type: str


class UserUpdate(BaseModel):
    email: EmailStr  # Позволяет изменить email
    name: str   # Позволяет изменить имя
