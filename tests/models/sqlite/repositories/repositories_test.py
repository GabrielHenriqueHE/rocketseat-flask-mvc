import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from src.models.sqlite.entities.pet import PetsTable
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.models.sqlite.repositories.pet_repository import PetRepository
from src.models.sqlite.settings.connection import DBConnectionHandler

@pytest.mark.skip(reason='Teste de integração com o banco de dados.')
def test_get_all_pets():
    connection_handler = DBConnectionHandler()
    connection_handler.connect()

    repo = PetRepository(connection_handler)

    response = repo.get_all_pets()
    print(response)

@pytest.mark.skip(reason='Teste de integração com o banco de dados.')
def test_delete_pet():
    connection_handler = DBConnectionHandler()
    connection_handler.connect()

    repo = PetRepository(connection_handler)

    pets_before_delete = repo.get_all_pets()
    print(pets_before_delete)

    repo.delete_pet('belinha')

    pets_after_delete = repo.get_all_pets()
    print(pets_after_delete)

    assert len(pets_after_delete) == len(pets_before_delete) - 1 

@pytest.mark.skip(reason='Teste de integração com o banco de dados.')
def test_get_person():
    connection_handler = DBConnectionHandler()
    connection_handler.connect()

    person_id: int = 1

    repo = PeopleRepository(connection_handler)

    response = repo.get_person(person_id)

    print(response)
