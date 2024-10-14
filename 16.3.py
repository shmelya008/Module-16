from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
async def welcome() -> dict:
    return {'message': 'Главная страница'}

@app.get("/user")
async def admin() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                   example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age',
                   example='24')]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f'The user {user_id} is registered'

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='24')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                      example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age',
                      example='24')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} has been updated'

@app.delete("/user/{user_id}")
async def user_del(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='24')]) -> str:
    users.pop(str(user_id))
    return f'Пользователь №{user_id} удалён'
