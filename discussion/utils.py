from storage.fake_db import fake_db
from uuid import uuid4
import json

# BD resoures
all_discussions = fake_db.get("discussions", {}).values()
all_users=fake_db.get("users", {}).values()
all_users_id=fake_db.get("users", {})


def search_discussion(contact):
    for discussion in all_discussions:
        if sorted(discussion.get("contacts")) == sorted(contact):
            return contact
    return None

def create_discussion(contacts, name):
    discussion_id=str(uuid4())
    all_discussions=fake_db.get("discussions", {})
    discussion= {"id" : discussion_id, "contacts" : contacts}
    discussion["id"] = discussion_id
    discussion["name"] = name
    all_discussions[discussion_id] = discussion

    with open("storage/discussion.json", "w") as file:
        json.dump(all_discussions, file, default=str)
    return discussion

def get_contact_discussions(user_id):
    contact_discussion=[]
    for discussion in all_discussions:
        contacts=discussion.get("contacts")
        if user_id in contacts:
            other_user = get_other_user(contacts, user_id)
            discussion["name"]=other_user["name"]

            contact_discussion.append(discussion)
    return contact_discussion

def get_other_user(contacts, user_id):
    for contact in contacts:
        if contact != user_id:
            return all_users_id.get(contact)
    return all_users_id.get(contacts[0])