from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from config.db import connection
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
import re

users = APIRouter()


@users.get("/users")
def find_all_users():
    list_users = usersEntity(connection.signai_app.users.find())
    return JSONResponse(
        content={"message": "Todo esta en orden", "data": list_users},
        status_code=200
    )


@users.post("/users")
def create_user(user: User):
    new_user = dict(user)
    del new_user["id"]

    username = new_user["username"]
    password = new_user["password"]
    email = new_user["email"]

    new_user["password"] = sha256_crypt.encrypt(password)

    if len(username) == 0 or len(password) == 0 or len(email) == 0:
        raise HTTPException(
            status_code=400, detail="Los campos Nombre de Usuario / Contraseña / Email no pueden ser vacios")

    search_user = connection.signai_app.users.find_one({"username": username})

    if search_user:
        raise HTTPException(
            status_code=400, detail="Ya existe un usuario registrado con ese Nombre de Usuario")

    if not validate_email(email):
        raise HTTPException(
            status_code=400, detail="Correo electronico incorrecto")

    if not validate_username(username):
        raise HTTPException(
            status_code=400, detail="Nombre de usuario incorrecto")

    user_created = connection.signai_app.users.insert_one(new_user)

    if user_created:
        return JSONResponse(
            content={"message": "Usuario Creado",
                     "data": str(user_created.inserted_id),
                     "codeStatus": 201},
            status_code=201
        )

    else:
        raise HTTPException(status_code=500, detail="Error creating user")


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
