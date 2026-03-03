import pytest
from http_client import get


@pytest.fixture
def client_get():
    return get