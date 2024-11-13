from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Feedback(BaseModel):
    name: str
    message: str

list_feedback = []

@app.post("/feedback")
async def add_feedback(feedback: Feedback):
    if feedback.name and feedback.message:
        list_feedback.append({'name':feedback.name, 'message':feedback.message})
        return {"message": "Feedback received. Thank you, "+feedback.name+"!"}