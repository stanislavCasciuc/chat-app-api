from pydantic import BaseModel

class Contact(BaseModel):
    name: str
    password: str
    id: str

