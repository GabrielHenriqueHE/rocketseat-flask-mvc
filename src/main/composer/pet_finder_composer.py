
from src.controllers.pet_finder_controller import PetFinderController
from src.models.sqlite.repositories.pet_repository import PetRepository
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.views.pet_finder_view import PetFinderView

def pet_finder_composer():
    connection_handler = DBConnectionHandler()
    connection_handler.connect()

    model = PetRepository(connection_handler)
    controller = PetFinderController(model)
    view = PetFinderView(controller)

    return view
