from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from config.db import connection
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from utils.validations import validate_email, validate_username
from utils.response import Response
from services.user_services import service_find_all_users, service_create_user

users = APIRouter()


@users.get("/users")
def find_all_users():
    response = service_find_all_users()
    response_dict = {
        "message": response.message,
        "codeStatus": response.code_status,
        "data": response.data
    }
    if not response_dict["codeStatus"] >= 400:
        return JSONResponse(content=response_dict, status_code=response_dict["codeStatus"])
    else:
        raise HTTPException(detail=response_dict["message"],
                            status_code=response_dict["codeStatus"])


@users.post("/users")
def create_user(user: User):
    new_user = dict(user)
    del new_user["id"]

    response = service_create_user(new_user)
    response_dict = {
        "message": response.message,
        "codeStatus": response.code_status,
        "data": response.data
    }
    if not response_dict["codeStatus"] >= 400:
        return JSONResponse(content=response_dict, status_code=response_dict["codeStatus"])
    else:
        raise HTTPException(detail=response_dict["message"],
                            status_code=response_dict["codeStatus"])
