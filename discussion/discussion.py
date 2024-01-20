from fastapi import APIRouter, HTTPException
from discussion.model import Discussion
from storage.fake_db import fake_db
from discussion.utils import search_discussion, create_discussion, get_contact_discussions

discussion_router = APIRouter()
@discussion_router.post("/api/discussions", response_model = Discussion )
def init_discussion(discussion_data:Discussion):
    contacts = list(set(discussion_data.contacts))

    users = fake_db.get("users", {})
    for contact in contacts:
        if not users.get(str(contact)):
            raise HTTPException(status_code=404, detail="NU E CONTACT")
    discussion=search_discussion(contacts)
    if discussion:
        raise HTTPException(status_code=404, detail="Discussion already exist")
    discussion_created=create_discussion(contacts, discussion_data.name)
    return discussion_created

@discussion_router.get("/api/discussions/")
def get_discussion(user_id: str = None):
    contact_discussions = get_contact_discussions(user_id)
    return contact_discussions






