import re

from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface

class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def create(self, person_info: dict) -> dict:
        first_name = person_info['first_name']
        last_name = person_info['last_name']
        age = person_info['age']
        pet_id = person_info['pet_id']

        self.__validate_names(first_name, last_name)

        self.__people_repository.insert_person(
            first_name=first_name,
            last_name=last_name,
            age=age,
            pet_id=pet_id
        )

        return self.__format_response(person_info)

    def __validate_names(self, first_name: str, last_name: str) -> None:
        non_valid_characters = re.compile(r'[^a-zA-Z]')

        if non_valid_characters.search(first_name) or non_valid_characters.search(last_name):
            raise ValueError("Os nomes só podem conter letras!")
        
    def __format_response(self, person_info: dict) -> dict:
        return {
            'data': {
                'type': 'person',
                'count': 1,
                'attributes': person_info
            }
        }