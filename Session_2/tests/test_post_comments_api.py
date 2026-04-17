import pytest
from validations.comments_api import validate_comment_for_post
from http_client import parse_json


@pytest.mark.parametrize("post_id", [1, 2])
def test_get_post_comments_ok(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}/comments")

    assert response.status_code == 200

    data = parse_json(response)

    assert isinstance(data, list)
    assert data

    for comment in data:
        validate_comment_for_post(comment, post_id)