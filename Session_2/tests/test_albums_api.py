import pytest
from validations.albums_api import validate_album_by_id


@pytest.mark.parametrize(
    "album_id",
    [1, 2]        
)
def test_get_album_by_id_ok(client_get, album_id):
    response = client_get(f"/albums/{album_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()
    validate_album_by_id(data, album_id)