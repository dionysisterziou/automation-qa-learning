def validate_comment_by_id(data, comment_id):
    assert data["id"] == comment_id, f"Expected {comment_id}, got {data['id']}"
    assert "email" in data, "Email field missing"
    assert isinstance(data["email"], str), "Email should be string"
    assert data["body"], "Body should not be empty"
    assert isinstance(data["postId"], int), "postId should be integer"