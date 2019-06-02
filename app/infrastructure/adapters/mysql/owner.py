from core.repositories.owner import OwnerQueryRepository, OwnerCommandRepository
from infrastructure.adapters.mysql.connection import connection_wrapper
from infrastructure.adapters.mysql.models import Owner


class OwnerMysqlAdapter(OwnerQueryRepository, OwnerCommandRepository):

    @connection_wrapper
    def list_the_owners(self):
        owners = Owner.select()
        data = [owner for owner in owners]
        return data

    @connection_wrapper
    def get_a_owner_by_id(self, id):
        try:
            data = Owner.get_by_id(id)
        except Exception as e:
            data = []
        finally:
            return data

    @connection_wrapper
    def register_a_owner(self, data):
        return Owner.create(**data)

    def enable_a_owner(self, owner_object):
        return self.update_owner(owner_object)

    def disable_a_owner(self, owner_object):
        return self.update_owner(owner_object)

    @connection_wrapper
    def update_owner(self, owner_object):
        data = Owner.save(owner_object)
        return data
