def task_5(object, particular_value):
    for key, value in object.items():
        if isinstance(value, list) and particular_value in value:
            return key
        elif isinstance(value, dict):
            result = task_5(value, particular_value)
            if result is not None:
                return key
    return None
