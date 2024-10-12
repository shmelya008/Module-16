from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {'message': 'Главная страница'}

@app.get("/user/admin")
async def admin() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get("/user/{user_id}")
async def userid(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get("/user")
async def user_info(username: str = 'name', age: int = 0) -> dict:
    return {'message': f'Информация о пользователе: Имя: {username}, Возраст: {age}'}
  
