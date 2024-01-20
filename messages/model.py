from pydantic import BaseModel

class Message(BaseModel):
    user_id:str
    discussion_id:str
    value:str
    time:str


