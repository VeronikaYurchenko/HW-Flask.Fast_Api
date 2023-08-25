# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT запросы с данными
# пользователей и обновлять их в базе данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Реализуйте валидацию данных запроса и ответа.
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, EmailStr, SecretStr
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

USERS = []


class User(BaseModel):
    id_: int
    name: str
    email: EmailStr
    password: SecretStr


@app.get('/users/')
async def all_users():
    return {'users': USERS}


@app.post('/user/add')
async def add_user(user: User):
    USERS.append(user)
    return {"user": user, "status": "added"}


@app.put('/user/update/{user_id}')
async def update_user(user_id: int, user: User):
    for item in USERS:
        if item.id_ == user_id:
            item.name = user.name
            item.email = user.email
            item.password = user.password
            return {"user": user, "status": "updated"}
    return HTTPException(404, 'User not found')


@app.delete('/user/delete/{user_id}')
async def delete_user(user_id: int):
    for item in USERS:
        if item.id_ == user_id:
            USERS.remove(item)
            return {"status": "success"}
    return HTTPException(404, 'User not found')


if __name__ == "__main__":
    uvicorn.run("task4:app", port=8000)
