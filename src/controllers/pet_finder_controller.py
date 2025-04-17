
from .interfaces.pet_finder_controller import PetFinderControllerInterface
from src.models.sqlite.entities.pet import PetsTable
from src.models.sqlite.interfaces.pet_repository import PetRepositoryInterface

class PetFinderController(PetFinderControllerInterface):
    def __init__(self, pet_repository: PetRepositoryInterface):
        self.__pet_repository = pet_repository
        
    def list_pets(self) -> dict:
        pets = self.__list_pets()

        return self.__format_response(pets)

    def __list_pets(self) -> list[PetsTable]:
        pets = self.__pet_repository.get_all_pets()

        return pets
    
    def __format_response(self, pets: list[PetsTable]) -> dict:
        formatted_pets = []

        for pet in pets:
            formatted_pets.append({
                'id': pet.id,
                'name': pet.name
            })

        return {
            'data': {
                'type': 'pet',
                'count': len(formatted_pets),
                'attributes': formatted_pets
            }
        }