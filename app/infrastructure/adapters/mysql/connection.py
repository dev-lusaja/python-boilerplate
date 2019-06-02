# -*- coding: utf-8 -*-
import os
from functools import wraps
from peewee import *


db = MySQLDatabase(os.getenv('MYSQL_DB', 'default'),
                   host=os.getenv('MYSQL_HOST', 'localhost'),
                   user=os.getenv('MYSQL_USER', 'root'),
                   password=os.getenv('MYSQL_PWD', '123456'),
                   port=int(os.getenv('MYSQL_PORT', 3306))
                   )


# Wrapper
def connection_wrapper(method):
    @wraps(method)
    def method_wrapper(*args, **kwargs):
        try:
            db.connect()
            return method(*args, **kwargs)
        except Exception as e:
            raise e
        finally:
            db.close()
    return method_wrapper
