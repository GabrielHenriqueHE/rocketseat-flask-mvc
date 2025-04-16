
from src.controllers.pet_finder_controller import PetFinderController
from src.models.sqlite.entities.pet import PetsTable

class MockPetRepository:
    def get_all_pets(self):
        return [
            PetsTable(id=1, name='Buddy', type='Dog'),
            PetsTable(id=2, name='Fluffy', type='Cat')
        ]
    
def test_list_pets():
    controller = PetFinderController(MockPetRepository())

    response = controller.list_pets()

    expected_response = {
        'data': {
                'type': 'pet',
                'count': 2,
                'attributes': [
                    {'id': 1, 'name': 'Buddy'},
                    {'id': 2, 'name': 'Fluffy'}
                ]
            }
    }

    assert response == expected_response