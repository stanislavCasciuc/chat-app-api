from fastapi import APIRouter, HTTPException

from storage.fake_db import fake_db
from users.models import UserCreate
from users.utils import create_user

register_router=APIRouter()
@register_router.post("/api/register")
def register_user(user_data: UserCreate):
   all_users=fake_db.get("users",{}).values()
   for user in all_users:
      if user_data.name == user["name"]:
         raise HTTPException(status_code=401, detail="User already registered")
   user=create_user(user_data)
   return user