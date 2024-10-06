from fastapi import APIRouter, Depends

from src.api.service.health_service import HealthService

router = APIRouter()


# Dependency injection
def get_health_service():
    return HealthService()


@router.get("/health")
def get_health_status(health_service: HealthService = Depends(get_health_service)):
    return health_service.check_health()
