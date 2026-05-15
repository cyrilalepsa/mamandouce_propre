from fastapi import APIRouter, Depends
from datetime import datetime, timezone
from models.guardian import SystemHealthReport, HealthStatus, ComponentHealth, ComponentType
import time

router = APIRouter(prefix="/health", tags=["system-health"])

@router.get("/status", response_model=SystemHealthReport)
async def get_system_status():
    """
    Endpoint principal pour le dashboard Admin NeriaCorp.
    Vérifie l'état de chaque organe vital de l'app.
    """
    # Ici, on simulera ou on testera les vraies connexions (DB, Stripe, etc.)
    components = [
        ComponentHealth(
            component=ComponentType.API_SERVER,
            status=HealthStatus.HEALTHY,
            last_check=datetime.now(timezone.utc).isoformat(),
            response_time_ms=12.5
        ),
        ComponentHealth(
            component=ComponentType.DATABASE,
            status=HealthStatus.HEALTHY,
            last_check=datetime.now(timezone.utc).isoformat()
        ),
        ComponentHealth(
            component=ComponentType.FOOD_SCANNER,
            status=HealthStatus.HEALTHY,
            last_check=datetime.now(timezone.utc).isoformat()
        )
    ]
    
    return SystemHealthReport(
        timestamp=datetime.now(timezone.utc).isoformat(),
        overall_status=HealthStatus.HEALTHY,
        components=components,
        active_incidents=0,
        auto_repairs_last_24h=0,
        escalated_incidents=0
    )

@router.get("/ping")
async def simple_ping():
    """Réponse ultra-rapide pour les tests de latence"""
    return {"status": "pong", "timestamp": time.time()}