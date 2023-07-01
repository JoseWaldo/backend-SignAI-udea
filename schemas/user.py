def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "password": user["password"]
    }


def usersEntity(users) -> list:
    return [userEntity(user) for user in users]
