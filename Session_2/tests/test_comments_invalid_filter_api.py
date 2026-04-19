from http_client import parse_json


def test_get_comments_invalid_post_id_filter_jsonplaceholder_returns_empty_list(api_client):
    # JSONPlaceholder fake API behavior:
    # invalid filter values return 200 with an empty list instead of a 400 validation error.
    response = api_client.get("/comments?postId=abc")

    assert response.status_code == 200

    data = parse_json(response)

    assert isinstance(data, list)
    assert data == []