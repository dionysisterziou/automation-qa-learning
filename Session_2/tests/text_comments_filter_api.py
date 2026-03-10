import pytest

@pytest.mark.parametrize(
    "post_id",
    [1, 2]
)
def test_get_comments_filter_api(client_get, post_id):
    response = client_get(f"/comments?postId={post_id}")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()

    assert isinstance(data, list), f"Expected list, got {type(data)}"
    assert data, "Empty list"

    for comment in data:
        assert comment["postId"] == post_id, f"Expected {post_id}, got {comment['postId']}"