from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# model
class User(BaseModel):
    name: str
    age: str

@app.post('/user')
async def add_user(user: User):
    if int(user.age) >= int(18):
        is_adult = True
    else:
        is_adult = False

    return {"name":user.name, "age": user.age, "is_adult": is_adult}