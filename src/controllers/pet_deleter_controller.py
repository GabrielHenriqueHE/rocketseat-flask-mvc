

from src.models.sqlite.interfaces.pet_repository import PetRepositoryInterface
from src.models.sqlite.entities.pet import PetsTable

class PetDeleterController:
    def __init__(self, pet_repository: PetRepositoryInterface):
        self.__pet_repository = pet_repository

    def delete(self, name: str) -> None:
        self.__pet_repository.delete_pet(name)

    