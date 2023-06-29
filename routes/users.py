from fastapi import APIRouter
from config.db import connection
from schemas.user import userEntity, usersEntity

users = APIRouter()


@users.get("/users")
def find_all_users():
    listUsers = usersEntity(connection.signai_app.users.find())
    return {"message": "All Ok", "codeStatus": 200, "data": listUsers}


@users.post("/users")
def create_user():
    return {
        "message": "Hello World!"
    }
