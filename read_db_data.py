import os
from fastapi import FastAPI, HTTPException
from databases import Database
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

with open('db_link.txt', 'r', encoding='utf-8') as file:
    db_link = file.read()

DATABASE_URL = db_link

database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup_database():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_database():
    await database.disconnect()



# Модель Liad для валидации исходящих данных
class LiadReturn(BaseModel):
    id: Optional[int] = None
    title: str
    
@app.get("/liad")
async def liad_list():
    query = ("SELECT id,title FROM profi")
    values = {}
    try:
        result = await database.fetch_one(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch user from database")
    if result:
        return LiadReturn(title=result["title"], id=result["id"])
    else:
        raise HTTPException(status_code=404, detail="User not found")