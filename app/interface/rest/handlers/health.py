from core.container import AppServices
from interface.rest.decorators import handler

health_services = AppServices.health()


@handler.wrapper
def get():
    rsp = health_services.get_status()
    error = False
    message = 'Success'
    http_code = 200
    return rsp, error, message, http_code
