from abc import ABCMeta, abstractmethod


class OwnerQueryRepository(metaclass=ABCMeta):

    @abstractmethod
    def list_the_owners(self):
        raise NotImplementedError

    @abstractmethod
    def get_a_owner_by_id(self, id):
        raise NotImplementedError


class OwnerCommandRepository(metaclass=ABCMeta):

    @abstractmethod
    def register_a_owner(self, data):
        raise NotImplementedError

    @abstractmethod
    def disable_a_owner(self, owner_object):
        raise NotImplementedError

    @abstractmethod
    def enable_a_owner(self, owner_object):
        raise NotImplementedError
