
from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface

from src.views.interfaces.view_interface import ViewInterface
from src.views.httptypes.http_request import HttpRequest
from src.views.httptypes.http_response import HttpResponse

class PetDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self.__controller = controller

    
    def handle(self, request: HttpRequest) -> HttpResponse:
        name = request.param['name']

        self.__controller.delete(name)

        return HttpResponse(status_code=204)