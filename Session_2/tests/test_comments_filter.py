import pytest
from http_client import parse_json
from validations.comments_api import validate_comment_for_post

@pytest.mark.parametrize(
    "post_id",
    [1, 2]
)
def test_get_comments_filter_by_post_ok(api_client, post_id):
    response = api_client.get(f"/comments?postId={post_id}")

    assert response.status_code == 200

    data = parse_json(response)

    assert isinstance(data, list)
    assert data

    for comment in data:
        validate_comment_for_post(comment, post_id)