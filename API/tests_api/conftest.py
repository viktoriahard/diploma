import pytest

from API.client.api_client import ApiClient


@pytest.fixture
def api_client():
    return ApiClient()