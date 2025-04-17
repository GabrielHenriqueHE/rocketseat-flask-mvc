
from src.controllers.pet_deleter_controller import PetDeleterController
from src.models.sqlite.repositories.pet_repository import PetRepository
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.views.pet_deleter_view import PetDeleterView

def pet_deleter_composer():
    connection_handler = DBConnectionHandler()
    connection_handler.connect()

    model = PetRepository(connection_handler)
    controller = PetDeleterController(model)
    view = PetDeleterView(controller)

    return view