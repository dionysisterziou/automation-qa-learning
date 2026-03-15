def test_get_comment_missing_resource(client_get):
    response = client_get("/comments/999999")

    assert response.status_code == 404