def validate_user(user):
    assert user["role"] == "admin", "User is not admin"
    assert user["active"], "User is not active"


user = {
    "role": "admin",
    "active": True
}


validate_user(user)