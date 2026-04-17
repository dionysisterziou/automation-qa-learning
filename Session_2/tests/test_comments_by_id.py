import pytest
from validations.comments_api import validate_comment_by_id

@pytest.mark.parametrize(
    "comment_id",
    [1, 2]
)
def test_get_comment_by_id_ok(api_client, comment_id):
    response = api_client.get(f"/comments/{comment_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()

    validate_comment_by_id(data, comment_id)