import datetime

from core.repositories.owner import OwnerQueryRepository, OwnerCommandRepository


class OwnerMock:
    def __init__(self):
        self.id = 'f0125ea4-3d16-4f37-977a-876bac03f451'
        self.name = 'Developer'
        self.status = 1
        self.regDate = datetime.datetime.strptime('2019-06-02T02:39:40+00:00', '%Y-%m-%dT%H:%M:%S+00:00')


class OwnerMockAdapter(OwnerQueryRepository, OwnerCommandRepository):

    def list_the_owners(self):
        owners = [OwnerMock() for owner in range(2)]
        return owners

    def get_a_owner_by_id(self, id):
        owner = OwnerMock()
        if owner.id == id:
            return owner
        else:
            return {}

    def register_a_owner(self, data):
        return OwnerMock()

    def enable_a_owner(self, owner_object):
        return self.update_owner(owner_object)

    def disable_a_owner(self, owner_object):
        return self.update_owner(owner_object)

    def update_owner(self, owner_object):
        return owner_object
