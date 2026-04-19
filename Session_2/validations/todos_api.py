def validate_todo_structure(data):
    assert isinstance(data, dict), "Todo response should be a dictionary"

    required_fields = ["userId", "id", "title", "completed"]
    for field in required_fields:
        assert field in data, f"Missing field: {field}"

    assert isinstance(data["userId"], int), "Todo userId should be int"
    assert isinstance(data["id"], int), "Todo id should be int"
    assert isinstance(data["title"], str), "Todo title should be str"
    assert isinstance(data["completed"], bool), "Todo completed should be bool"