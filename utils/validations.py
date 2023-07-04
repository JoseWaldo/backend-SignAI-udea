import re


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


def validate_username(username):
    pattern = r'^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'
    if re.match(pattern, username):
        return True
    else:
        return False
