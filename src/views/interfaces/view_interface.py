from abc import ABC, abstractmethod

from src.views.httptypes.http_request import HttpRequest
from src.views.httptypes.http_response import HttpResponse

class ViewInterface(ABC):

    @abstractmethod
    def handle(self, request: HttpRequest) -> HttpResponse:
        pass