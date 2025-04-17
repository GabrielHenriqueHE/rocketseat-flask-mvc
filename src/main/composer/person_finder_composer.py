
from src.controllers.person_finder_controller import PersonFinderController
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.views.person_finder_view import PersonFinderView

def person_finder_composer():
    connection_handler = DBConnectionHandler()
    connection_handler.connect()

    model = PeopleRepository(connection_handler)
    controller = PersonFinderController(model)
    view = PersonFinderView(controller)

    return view