# Placeholder for API tests
# Directory: tests/test_api.py
from utils.api_client import APIClient
from utils.orm import save_test_result
import pytest

@pytest.mark.parametrize("endpoint, payload, expected_status", [
    ("/api/login", {"username": "user1", "password": "pass1"}, 200),
    ("/api/login", {"username": "user2", "password": "wrongpass"}, 401),
    ("/api/data", {}, 403)
])
def test_api(endpoint, payload, expected_status):
    client = APIClient("https://example.com")
    response = client.post(endpoint, payload)
    assert response.status_code == expected_status
    save_test_result(f"test_api_{endpoint}", "Passed" if response.status_code == expected_status else "Failed")
