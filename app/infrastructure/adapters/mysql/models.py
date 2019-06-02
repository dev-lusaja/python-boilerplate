# -*- coding: utf-8 -*-
from peewee import *
from infrastructure.adapters.mysql.connection import db


# Models
class BaseModel(Model):

    class Meta:
        database = db


class Owner(BaseModel):
    id = CharField(primary_key=True, max_length=50)
    name = CharField(null=False, unique=True, max_length=50)
    status = SmallIntegerField(null=False)
    regDate = DateTimeField(null=False)


# Populate tables and close session
db.create_tables([Owner])
db.close()
