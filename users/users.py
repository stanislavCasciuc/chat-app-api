from fastapi import APIRouter, HTTPException

from storage.fake_db import fake_db
from users.models import UserCreate
from users.utils import create_user
from users.utils import get_user_data
login_router = APIRouter()




@login_router.post("/api/authenticate")
def authenticate_user(user_data: UserCreate):
   user = get_user_data(user_data)
   print(user)
   if user==None:
      raise HTTPException(status_code=401, detail="Incorrect username or password")
   return user


