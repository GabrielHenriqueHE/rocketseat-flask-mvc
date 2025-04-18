
from .interfaces.person_finder_controller import PersonFinderControllerInterface
from src.errors.errortypes.http_not_found import HttpNotFoundError
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.repositories.people_repository import PeopleRepositoryInterface

class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def find(self, person_id: int) -> dict:
        person = self.__find_person(person_id)

        return self.__format_response(person)

    def __find_person(self, person_id: int) -> PeopleTable:
        person = self.__people_repository.get_person(person_id)

        if not person:
            raise HttpNotFoundError('Pessoa não encontrada!')

        return person
        

    def __format_response(self, person: PeopleTable) -> dict:
        return {
            'data': {
                'type': 'person',
                'count': 1,
                'attributes': {
                    'first_name': person.first_name,
                    'last_name': person.last_name,
                    'pet_name': person.pet_name,
                    'pet_type': person.pet_type
                }
            }
        }