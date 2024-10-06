import pytest
from unittest.mock import MagicMock
from src.api.service.health_service import HealthCheckService

@pytest.fixture
def db_connection_mock():
    return MagicMock(name="db_connection")

def test_health_check_service_init(db_connection_mock):
    service = HealthCheckService(db_connection_mock)
    assert service.db == db_connection_mock

def test_check_health_success(db_connection_mock):
    service = HealthCheckService(db_connection_mock)
    db_connection_mock.cursor.return_value.__enter__.return_value.execute.return_value = None
    response = service.check_health()
    assert response.status == "OK"
    assert response.dependencies == {"database": "Connected"}

def test_check_health_failure(db_connection_mock):
    service = HealthCheckService(db_connection_mock)
    db_connection_mock.cursor.return_value.__enter__.return_value.execute.side_effect = Exception("Mocked error")
    response = service.check_health()
    assert response.status == "OK"
    assert response.dependencies == {"database": "Failed to connect to database: Mocked error"}
