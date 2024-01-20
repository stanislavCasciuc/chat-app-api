
def create_new_chat(disscusion_id, name, value, all_messages):
    message={"name":name, "value":value}
    all_messages[disscusion_id]=message

    return message
