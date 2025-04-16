from abc import ABC, abstractmethod
from typing import List

class PetRepositoryInterface(ABC):
    
    @abstractmethod
    def get_all_pets(self) -> List:
        pass

    @abstractmethod
    def delete_pet(self, name: str) -> None:
        pass
