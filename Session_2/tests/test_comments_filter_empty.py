from http_client import parse_json


def test_get_comments_filter_empty(api_client):
    response = api_client.get("/comments?postId=9999")

    assert response.status_code == 200

    data = parse_json(response)

    assert isinstance(data, list)
    assert data == []