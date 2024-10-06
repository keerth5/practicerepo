from src.api.model.health_check import HealthCheckResponse
from src.api.repository import user_repository


class HealthService:
    def check_health(self):
        """
        Runs all health checks and returns a HealthCheckResponse object.

        The response's status will be "OK" if all checks pass, otherwise it will
        be "ERROR". The dependencies dictionary will contain the results of each
        check.

        :return: A HealthCheckResponse object
        :rtype: HealthCheckResponse
        """
        response = HealthCheckResponse(status="OK")
        dependencies = {
            "database": user_repository.check_db_connection(),
        }
        for name, status in dependencies.items():
            if status != "Connected":
                response.status = "ERROR"
            response.add_detail(name, status)
        return response
