from pytest_mock import mocker

from src.controllers.pet_deleter_controller import PetDeleterController

def test_delete_pet(mocker):
    mock_repository = mocker.Mock()

    controller = PetDeleterController(mock_repository)

    controller.delete('Buddy')

    mock_repository.delete_pet.assert_called_once_with('Buddy')