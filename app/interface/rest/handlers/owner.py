from core.container import AppServices
from interface.rest.decorators import handler


owner_service = AppServices.owner()


@handler.wrapper
def get():
    rsp = owner_service.list_the_owners()
    error = False
    message = 'Success'
    http_code = 200
    return rsp, error, message, http_code


@handler.wrapper
def get_by_id(id):
    rsp = owner_service.get_a_owner(id)
    error = False
    message = 'Success'
    http_code = 200
    return rsp, error, message, http_code


@handler.wrapper
def post(data):
    rsp = owner_service.register_a_owner(data)
    error = False
    message = 'Success'
    http_code = 200
    return rsp, error, message, http_code


@handler.wrapper
def delete(id):
    rsp = owner_service.disable_a_owner(id)
    error = False
    message = 'Success'
    http_code = 200
    return rsp, error, message, http_code


@handler.wrapper
def enable(id):
    rsp = owner_service.enable_a_owner(id)
    error = False
    message = 'Success'
    http_code = 200
    return rsp, error, message, http_code


@handler.wrapper
def disable(id):
    rsp = owner_service.disable_a_owner(id)
    error = False
    message = 'Success'
    http_code = 200
    return rsp, error, message, http_code
