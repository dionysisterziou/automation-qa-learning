import pytest
from validations.albums_api import validate_album_by_id
from http_client import parse_json


@pytest.mark.parametrize(
    "album_id",
    [1, 2]        
)
def test_get_album_by_id_ok(api_client, album_id):
    response = api_client.get(f"/albums/{album_id}")

    assert response.status_code == 200

    data = parse_json(response)

    validate_album_by_id(data, album_id)