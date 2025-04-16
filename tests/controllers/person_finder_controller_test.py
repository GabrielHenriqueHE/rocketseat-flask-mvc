from src.controllers.person_finder_controller import PersonFinderController

class MockPerson:
    def __init__(self, first_name, last_name, pet_name, pet_type):
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type

class MockPeopleRepository:
    def __init__(self):
        pass

    def get_person(self, person_id: int) -> MockPerson:
        return MockPerson('John', 'Doe', 'Fido', 'Dog')
    
def test_find_person():
    controller = PersonFinderController(MockPeopleRepository())

    person_id = 1

    response = controller.find(person_id)

    print(response)

    assert response == {
        'data': {
            'type': 'person',
            'count': 1,
            'attributes': {
                'first_name': 'John',
                'last_name': 'Doe',
                'pet_name': 'Fido',
                'pet_type': 'Dog'
            }
        }
    }