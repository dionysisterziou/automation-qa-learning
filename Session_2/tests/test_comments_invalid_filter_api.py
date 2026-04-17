from http_client import parse_json


def test_get_comments_invalid_filter_api(api_client):
    response = api_client.get("/comments?postId=abc")

    assert response.status_code == 200

    data = parse_json(response)

    assert isinstance(data, list)
    assert data == []