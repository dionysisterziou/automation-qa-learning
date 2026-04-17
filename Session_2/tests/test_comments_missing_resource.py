from http_client import parse_json


def test_get_comment_missing_resource(api_client):
    response = api_client.get("/comments/999999")

    assert response.status_code == 404

    data = parse_json(response)
    assert data == {}