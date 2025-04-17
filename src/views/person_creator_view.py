
from src.controllers.interfaces.person_creator_controller import PersonCreatorControllerInterface

from src.views.interfaces.view_interface import ViewInterface
from src.views.httptypes.http_request import HttpRequest
from src.views.httptypes.http_response import HttpResponse

class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self.__controller = controller

    
    def handle(self, request: HttpRequest) -> HttpResponse:
        data = request.body

        response = self.__controller.create(data)

        return HttpResponse(status_code=201, body=response)