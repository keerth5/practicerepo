import pytest
from unittest.mock import patch
from src.api.service.health_service import HealthService
from src.api.model.health_check import HealthCheckResponse

@pytest.fixture
def health_service():
    return HealthService()

def test_check_health_all_ok(health_service):
    with patch('src.api.repository.user_repository.check_db_connection', return_value="Connected"):
        response = health_service.check_health()
        
        assert isinstance(response, HealthCheckResponse)
        assert response.status == "OK"
        assert response.dependencies == {"database": "Connected"}

def test_check_health_database_error(health_service):
    with patch('src.api.repository.user_repository.check_db_connection', return_value="Failed to connect"):
        response = health_service.check_health()
        
        assert isinstance(response, HealthCheckResponse)
        assert response.status == "ERROR"
        assert response.dependencies == {"database": "Failed to connect"}
