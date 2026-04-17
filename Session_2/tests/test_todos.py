import pytest
from validations.todos_api import validate_todo_by_id
from http_client import parse_json


@pytest.mark.parametrize(
    "todo_id",
    [1, 2]
)
def test_get_todo_by_id_ok(api_client, todo_id):
    response = api_client.get(f"/todos/{todo_id}")

    assert response.status_code == 200

    data = parse_json(response)

    validate_todo_by_id(data, todo_id)