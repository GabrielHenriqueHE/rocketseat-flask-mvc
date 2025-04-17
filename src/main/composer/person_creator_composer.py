
from src.controllers.person_creator_controller import PersonCreatorController
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.views.person_creator_view import PersonCreatorView

def person_creator_composer():
    connection_handler = DBConnectionHandler()
    connection_handler.connect()

    model = PeopleRepository(connection_handler)
    controller = PersonCreatorController(model)
    view = PersonCreatorView(controller)

    return view