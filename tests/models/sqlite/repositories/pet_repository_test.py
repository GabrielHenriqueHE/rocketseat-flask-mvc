import pytest
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.pet import PetsTable
from src.models.sqlite.repositories.pet_repository import PetRepository

class MockConnection:
    def __init__(self):
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

class MockConnectionNoResults:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found.")

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

def test_delete_pets():
    mock_connection = MockConnection()

    repo = PetRepository(mock_connection)

    repo.delete_pet('petName')

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == 'petName')
    mock_connection.session.delete.assert_called_once()

def test_get_all_pets_no_results():
    mock_connection = MockConnectionNoResults()
    repo = PetRepository(mock_connection)

    response = repo.get_all_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []

def test_delete_pet_error_rollback():
    mock_connection = MockConnectionNoResults()
    repo = PetRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_pet('petName')
    
    mock_connection.session.rollback.assert_called_once()