# при получении GET-запроса по дополнительному маршруту `/users` возвращала бы JSON с данными о пользователе (юзере)

from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# model
class User(BaseModel):
    id: int
    name: str = "John"


# example data model
external_data = {
    "id": "123",
    "name": "John"
}

@app.get('/users')
async def return_users():
    return external_data