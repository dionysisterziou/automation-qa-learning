def validate_user_by_id(data, expected_id):
    assert isinstance(data, dict)
    assert "username" in data, "Username does not exist"
    assert "email" in data, "Email does not exist"
    assert data["id"] == expected_id, f"Expected id={expected_id}, got {data['id']}"