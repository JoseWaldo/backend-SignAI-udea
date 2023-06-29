def userEntity(user) -> dict:
    return {
        "id": user["_id"],
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
    }


def usersEntity(users) -> list:
    [userEntity(user) for user in users]
