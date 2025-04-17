
from src.controllers.interfaces.pet_finder_controller import PetFinderControllerInterface

from src.views.interfaces.view_interface import ViewInterface
from src.views.httptypes.http_request import HttpRequest
from src.views.httptypes.http_response import HttpResponse

class PetFinderView(ViewInterface):
    def __init__(self, controller: PetFinderControllerInterface) -> None:
        self.__controller = controller

    
    def handle(self, request: HttpRequest) -> HttpResponse:
        response = self.__controller.list_pets()

        return HttpResponse(status_code=200, body=response)