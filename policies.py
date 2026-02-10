def allowed_to_act(task):
    blocked = ["login", "send money", "post publicly"]
    return not any(b in task.lower() for b in blocked)
