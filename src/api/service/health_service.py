from src.api.repository.user_repository import check_db_connection
from src.api.model.health_check import HealthCheckResponse

class HealthService:
    def __init__(self):
        self.dependencies = {
            "database": check_db_connection,
        }

    def check_health(self):
        """
        Performs a health check on all the service's dependencies.

        Returns a HealthCheckResponse containing the status of all the service's dependencies.
        """
        response = HealthCheckResponse(status="OK")
        for name, check_func in self.dependencies.items():
            response.add_detail(name, check_func())
        return response

