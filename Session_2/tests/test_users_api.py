import pytest
from http_client import get
from validations.users_api import validate_user_by_id

@pytest.mark.parametrize(
    "expected_id",
    [
        1,
        2
    ]
)
def test_get_user_by_id_ok(expected_id):
    response = get(f"/users/{expected_id}") # timeout=5 μπαίνει default από http_client
    data = response.json()

    assert response.status_code == 200, f"Expected final 200, got {response.status_code}"
    validate_user_by_id(data, expected_id)