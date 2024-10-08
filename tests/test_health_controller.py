from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from src.api.controller.health_controller import router
from src.api.model.health_check import HealthCheckResponse


@pytest.fixture
def test_client():
    return TestClient(router)


@pytest.fixture
def mock_health_service():
    with patch("src.api.controller.health_controller.HealthService") as mock:
        yield mock.return_value


def test_get_health_status_ok(test_client, mock_health_service):
    mock_response = HealthCheckResponse(status="OK")
    mock_response.add_detail("database", "Connected")
    mock_health_service.check_health.return_value = mock_response

    response = test_client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "OK",
        "dependencies": {"database": "Connected"},
    }
    mock_health_service.check_health.assert_called_once()


def test_get_health_status_error(test_client, mock_health_service):
    mock_response = HealthCheckResponse(status="ERROR")
    mock_response.add_detail("database", "Failed to connect")
    mock_health_service.check_health.return_value = mock_response

    response = test_client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ERROR",
        "dependencies": {"database": "Failed to connect"},
    }
    mock_health_service.check_health.assert_called_once()
