from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from src.models.sqlite.entities.pet import PetsTable
from src.models.sqlite.repositories.pet_repository import PetRepository

class MockConnection:
    def __init__(self):
        super().__init__()
        self.session = UnifiedAlchemyMagicMock(
            data = [(
                [mock.call.query(PetsTable)],
                [
                    PetsTable(id=1, name='dog', type='dog'), 
                    PetsTable(id=2, name='cat', type='cat')
                 ]
            )]
        )

    def __enter__(self): return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): pass


def test_get_all_pets():
    mock_connection = MockConnection()

    repo = PetRepository(mock_connection)

    response = repo.get_all_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == 'dog'