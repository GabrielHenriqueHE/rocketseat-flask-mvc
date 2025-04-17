import pytest

from pydantic import ValidationError

from src.errors.errortypes.http_unprocessable_entity import HttpUnprocessableEntityError
from src.validators.person_creator_validator import person_creator_validator

class MockRequest:
    def __init__(self, body: dict):
        self.body = body

def test_person_creator_validator():
    request = MockRequest({
        "first_name": "John",
        "last_name": "Doe",
        "age": 12,
        "pet_id": 1
    })

    person_creator_validator(request)
    
def test_person_creator_validator_with_errors():
    request = MockRequest({
        "first_name": "John",
        "last_name": "Doe",
        "age": '',
        "pet_id": 1
    })

    with pytest.raises(HttpUnprocessableEntityError) as exc:
        person_creator_validator(request)

    print(exc.value.message)