import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from src.api.controller import health_controller
from src.api.service.health_service import HealthService
from fastapi import FastAPI

# Create a FastAPI app and include the router
app = FastAPI()
app.include_router(health_controller.router)

client = TestClient(app)

# Test case
def test_get_health_status():
    # Create a mock for HealthService
    mock_health_service = MagicMock(spec=HealthService)

    # Mock the health check to return a more detailed response
    # Assuming the actual health check returns something like this:
    mock_health_service.check_health.return_value = {
        "status": "OK",
        "dependencies": {
            "database": "Connected"
        }
    }

    # Patch both the check_db_connection function and get_health_service (dependency injection)
    # Ensure check_db_connection is patched where it is used (i.e., in the HealthService)
    with patch('src.api.repository.user_repository.check_db_connection', return_value="Connected"), \
         patch('src.api.controller.health_controller.get_health_service', return_value=mock_health_service):

        # Make the GET request
        response = client.get("/health")

        # Assert that the status code is correct
        assert response.status_code == 200

        # Assert that the returned JSON matches the expected structure
        expected_response = {
            "status": "OK",
            "dependencies": {
                "database": "Connected"
            }
        }
        assert response.json() == expected_response

    # Assert that check_health was called once
    mock_health_service.check_health.assert_called_once()
