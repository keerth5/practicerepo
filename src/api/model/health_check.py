from pydantic import BaseModel

class HealthCheckResponse(BaseModel):
    status: str
    dependencies: dict = {}

    def add_detail(self, key, value):
        self.dependencies[key] = value
