from fastapi import APIRouter

users = APIRouter()


@users.get("/users")
def find_all_users():
    return {
        "message": "Hello World!"
    }


@users.post("/users")
def find_all_users():
    return {
        "message": "Hello World!"
    }
