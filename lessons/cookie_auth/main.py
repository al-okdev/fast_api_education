from fastapi import FastAPI, Cookie, Response
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

user_db = [
    {
        "username": "alex",
        "password": "pas123"
    },
    {
        "username": "oleg",
        "password": "pas456"
    }
]

@app.post('/login')
async def login(user: User, response: Response):
    for u in user_db:
        if u['username'] == user.username and u['password'] == user.password:
            response.set_cookie(key="session_tocken", value='abc123xyz456', secure=True, httponly=True)
            return user
        else:
            return {'error'}
    

@app.get('/user')
async def return_user(response: Response, session_tocken = Cookie()):
    if session_tocken:
        return 'ok'

    return Response(status_code=404, content='Пользователь не найден')

    response.status_code = 401
    return {'message': 'Unauthorized'}