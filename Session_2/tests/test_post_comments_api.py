import pytest
from validations.post_comments_api import validate_comment


@pytest.mark.parametrize(
    "post_id",
    [1, 2]
)
def test_get_post_comments_ok(client_get, post_id):
    response = client_get(f"/posts/{post_id}/comments")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()

    assert isinstance(data, list)
    assert data

    for comment in data:
        validate_comment(comment, post_id)