from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int | None
    is_subscribed: bool | None

@app.post("/create_user")
async def create_user(User: UserCreate):
    return User