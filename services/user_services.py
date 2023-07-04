from schemas.user import userEntity, usersEntity
from utils.validations import validate_email, validate_username
from passlib.hash import sha256_crypt
from config.db import connection
from utils.response import Response


def service_find_all_users() -> Response:
    try:
        list_users = usersEntity(connection.signai_app.users.find())
        return Response(list_users, 200, "Operación de busqueda exitosa!")
    except:
        return Response(None, 500, "Hubo un error al ejecutar la busqueda")


def service_create_user(new_user) -> Response:
    username = new_user["username"]
    password = new_user["password"]
    email = new_user["email"]

    new_user["password"] = sha256_crypt.encrypt(password)

    if len(username) == 0 or len(password) == 0 or len(email) == 0:
        return Response(None, 400, "Los campos Nombre de Usuario / Contraseña / Email no pueden ser vacios")

    try:
        search_user = connection.signai_app.users.find_one(
            {"username": username})
        if search_user:
            return Response(None, 400, "Ya existe un usuario registrado con ese Nombre de Usuario")
    except:
        return Response(None, 500, "Error al buscar al usuario")

    if not validate_email(email):
        return Response(None, 400, "Correo electronico incorrecto")

    if not validate_username(username):
        return Response(None, 400, "Nombre de usuario incorrecto")

    try:
        user_created = connection.signai_app.users.insert_one(new_user)
        if user_created:
            return Response(str(user_created.__inserted_id), 201, "Usuario Creado")
        else:
            return Response(None, 500, "Error al crear usuario")
    except:
        return Response(None, 500, "Error al crear usuario")
