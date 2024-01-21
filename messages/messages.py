from uuid import uuid4

from fastapi import APIRouter
import json
from messages.model import Message
from storage.fake_db import *



messages_router=APIRouter()

@messages_router.get("/api/messages/")
def get_messages(discussion_id:str):
    all_messages=fake_db.get("messages", {})
    user_messages=all_messages.get(discussion_id)
    if not user_messages:
        return
    return user_messages

# @messages_router.post("/api/messages", response_model=Message )
# def messages_post(discussion_id, user_id, value):
#     all_messages = fake_db.get("messages", {})
#     user=fake_db.get("users", {}).get(user_id)
#     user_name=user["name"]
#     message=Message(name=user_name, value=value)
#     if discussion_id not in all_messages:
#         all_messages[discussion_id] = []
#     message=message.model_dump()
#     all_messages[discussion_id].append(message)
#     with open("storage/messages.json", "w") as file:
#         json.dump(all_messages, file, default=str)
#     return message

@messages_router.post("/api/messages" )
def messages_post(message_obj:Message):
    all_messages = fake_db.get("messages", {})
    user=fake_db.get("users", {}).get(message_obj.user_id)
    user_name=user.get("name","")
    message = {
        "message_id":str(uuid4()),
        "user_id":message_obj.user_id,
        "name": user_name,
        "value":message_obj.value,
        "time":message_obj.time
        }
    if message_obj.discussion_id not in all_messages:
        all_messages[message_obj.discussion_id]=[]

    all_messages[message_obj.discussion_id].append(message)
    with open("storage/messages.json", "w") as file:
        json.dump(all_messages, file, default=str)
    return message


