from fastapi import FastAPI, Path, status, Body, HTTPException, Request, Form
from typing import Annotated, Type
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
def admin(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get("/user/{id}")
def admin(request: Request, id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[id - 1]})


@app.post("/user/{username}/{age}")
def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
             age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> str:
    key = 'id'
    max_id = max((item.get(key) for item in users if key in item), default=0)
    id = int(max_id + 1)
    users.append({'id': id, 'username': username, 'age': age})
    return f'Пользователь id {id} добавлен'


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')],
                username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                age: Annotated[int, Path(ge=18, le=120, description='Enter age')]):
    new_dict = {'id': user_id, 'username': username, 'age': age}
    for index, d in enumerate(users):
        if d.get('id') == user_id:
            users[index] = new_dict
            return users
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def user_del(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')]) -> User:
    for i in users:
        if i['id'] == user_id:
            users.remove(i)
            return i
    raise HTTPException(status_code=404, detail="User was not found")


add_user('UrbanUser', 24)
add_user('UrbanTest', 36)
add_user('Admin', 42)
add_user('UrbanProfi', 28)
