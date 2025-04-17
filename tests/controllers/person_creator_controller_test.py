import pytest

from src.controllers.person_creator_controller import PersonCreatorController
from src.errors.errortypes.http_bad_request import HttpBadRequestError

class MockPeopleRepository:
    def __init__(self):
        pass

    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass


def test_create_person():
    controller = PersonCreatorController(MockPeopleRepository())

    person = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 30,
        'pet_id': 1
    }

    response = controller.create(person)

    print(response)

    assert response['data']['type'] == 'person'
    assert response['data']['count'] == 1
    assert response['data']['attributes'] == person

def test_create_person_with_error():
    controller = PersonCreatorController(MockPeopleRepository())

    person = {
        'first_name': 'Jo12 hn',
        'last_name': 'Doe',
        'age': 30,
        'pet_id': 1
    }

    with pytest.raises(HttpBadRequestError) as exc:
        controller.create(person)

    assert str(exc.value) == 'Os nomes só podem conter letras!'
