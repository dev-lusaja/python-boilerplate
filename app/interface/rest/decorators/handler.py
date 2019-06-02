# -*- coding: utf-8 -*-
from functools import wraps
from interface.helpers.logger import ConsoleLogger as Log


def wrapper(method):
    @wraps(method)
    def method_wrapper(*args, **kwargs):
        try:
            rsp, error, message, http_code = method(*args, **kwargs)
        except Exception as e:
            rsp = []
            error = e.__class__.__name__
            message = e.__str__()
            http_code = 500
            Log().output(e)
        finally:
            return rsp, error, message, http_code
    return method_wrapper
