from pydantic import BaseModel

class Discussion(BaseModel):
    id: str=None
    contacts: list
    name: str

