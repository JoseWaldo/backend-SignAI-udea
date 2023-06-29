from fastapi import APIRouter

users = APIRouter()


@users.get("/")
def helloWorld():
    return {
        "message": "Hello World!"
    }
