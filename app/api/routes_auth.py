from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import create_token


router = APIRouter()

class AuthINput(BaseModel):
    username: str
    password: str


@router.post('/login')
def login(auth: AuthINput):
    if (auth.username == 'admin') and (auth.password == 'admin'):
        token = create_token({'sub': auth.username})
        return {'access_token': token}
    return {'error': 'Invalid Credentials'}