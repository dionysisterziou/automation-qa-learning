def test_get_comments_filter_empty(client_get):

    response = client_get("/comments?postId=9999")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert data == []