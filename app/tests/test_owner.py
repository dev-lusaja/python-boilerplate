from infrastructure.adapters.mock.owner import OwnerMockAdapter
from core.services.owner import OwnerService

owner_service = OwnerService(db_adapter=OwnerMockAdapter())


def test_list_the_owners():
    expected = [{'name': 'Developer', 'status': 1,
                 'id': 'f0125ea4-3d16-4f37-977a-876bac03f451', 'regDate': '2019-06-02 02:39:40'
                 },
                {'name': 'Developer', 'status': 1,
                 'id': 'f0125ea4-3d16-4f37-977a-876bac03f451', 'regDate': '2019-06-02 02:39:40'
                 }
                ]
    assert expected == owner_service.list_the_owners()


def test_get_a_owner():
    expected = {'name': 'Developer',
                'status': 1,
                'id': 'f0125ea4-3d16-4f37-977a-876bac03f451',
                'regDate': '2019-06-02 02:39:40'
                }
    assert expected == owner_service.get_a_owner('f0125ea4-3d16-4f37-977a-876bac03f451')
