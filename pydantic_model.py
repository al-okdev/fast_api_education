from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    username: str
    message: str
    
@app.post("/")
async def root(user: User):
    '''тут мы можем с переменной user, которая в себе содержит объект класса User с соответствующими полями (и указанными типами), делать любую логику
    - например, мы можем сохранить информацию в базу данных
    - или передать их в другую функцию
    - или другое'''
    print(f'Мы получили от юзера {user.username} такое сообщение: {user.message}') # тут мы просто выведем полученные данные на экран в отформатированном варианте
    return user # или можем вернуть обратно полученные данные, как символ того, что данные получили, или другая логика на ваш вкус