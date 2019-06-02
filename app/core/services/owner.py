from typing import Union

from core.repositories.owner import OwnerQueryRepository, OwnerCommandRepository
from core.schemas.owner import OwnerSchema, OwnerSchemaException


class OwnerService:

    __db_adapter = None
    __schema = OwnerSchema()

    def __init__(self, db_adapter: Union[OwnerQueryRepository, OwnerCommandRepository]):
        self.__db_adapter = db_adapter

    def list_the_owners(self):
        data = self.__db_adapter.list_the_owners()
        schema = self.__schema.dump(data, many=True)
        if schema.errors:
            raise OwnerSchemaException(schema.errors)
        return schema.data

    def get_a_owner(self, id):
        data = self.__db_adapter.get_a_owner_by_id(id)
        schema = self.__schema.dump(data)
        if schema.errors:
            raise OwnerSchemaException(schema.errors)
        return schema.data

    def register_a_owner(self, data):
        schema = self.__schema.load(data)
        if schema.errors:
            raise OwnerSchemaException(schema.errors)
        data = self.__db_adapter.register_a_owner(schema.data)
        return schema.data

    def enable_a_owner(self, id):
        owner_object = self.__db_adapter.get_a_owner_by_id(id)

        if not owner_object:
            raise Exception('The id was not found')

        schema = self.__schema.dump(owner_object)
        if schema.errors:
            raise OwnerSchemaException(schema.errors)

        owner_object.status = 1  # enable the owner
        result = self.__db_adapter.enable_a_owner(owner_object)

        if result == 1:
            return schema.data
        else:
            raise Exception('the Owner was not enabled')

    def disable_a_owner(self, id):
        owner_object = self.__db_adapter.get_a_owner_by_id(id)

        if not owner_object:
            raise Exception('The id was not found')

        schema = self.__schema.dump(owner_object)
        if schema.errors:
            raise OwnerSchemaException(schema.errors)

        owner_object.status = 0  # disable the owner
        result = self.__db_adapter.disable_a_owner(owner_object)

        if result == 1:
            return schema.data
        else:
            raise Exception('the Owner was not disabled')
