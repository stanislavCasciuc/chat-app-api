import json


def init_fake_bd():
    return {
        "users": init_data_from_file("storage/users.json"),
        "discussions": init_data_from_file("storage/discussion.json"),
        "messages": init_data_from_file("storage/messages.json")
    }
def init_data_from_file(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except:
        return {}

fake_db=init_fake_bd()


