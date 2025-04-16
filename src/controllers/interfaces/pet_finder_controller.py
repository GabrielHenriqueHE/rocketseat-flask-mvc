from abc import ABC, abstractmethod

class PetFinderControllerInterface(ABC):

    @abstractmethod        
    def list_pets(self) -> dict:
        pass