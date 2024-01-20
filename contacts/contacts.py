from fastapi import APIRouter, HTTPException
from contacts.models1 import Contact
from storage.fake_db import fake_db

contacts_router = APIRouter()

@contacts_router.get("/api/contacts")
def get_all_contacts():
    contacts = list(fake_db.get("users", {}).values())
    return contacts

@contacts_router.get("/api/contacts/{contact_id}", response_model=Contact)
def get_contact_by_id(contact_id: str):
    contact = fake_db.get("users", {}).get(contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact