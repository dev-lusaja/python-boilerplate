import dependency_injector.containers as containers
import dependency_injector.providers as providers

# Services
from core.services.owner import OwnerService
from core.services.health import HealthService

# Adapters
from infrastructure.adapters.mysql.owner import OwnerMysqlAdapter


# App Services
class AppServices(containers.DeclarativeContainer):
    health = providers.Factory(HealthService)
    owner = providers.Factory(OwnerService, db_adapter=OwnerMysqlAdapter())
