def validate_album_structure(data):
    assert isinstance(data, dict), "Album response should be a dictionary"

    required_fields = ["userId", "id", "title"]
    for field in required_fields:
        assert field in data, f"Missing field: {field}"

    assert isinstance(data["userId"], int), "Todo userId should be int"
    assert isinstance(data["id"], int), "Todo id should be int"
    assert isinstance(data["title"], str), "Todo title should be str"