user = {
    "id": 123,
    "role": "admin",
    "active": True
}

assert user["role"] == "admin", "User is not admin"
assert user["active"], "User is not active"