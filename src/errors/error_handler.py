
from src.errors.errortypes.http_bad_request import HttpBadRequestError
from src.errors.errortypes.http_not_found import HttpNotFoundError
from src.errors.errortypes.http_unprocessable_entity import HttpUnprocessableEntityError
from src.views.httptypes.http_response import HttpResponse


def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntityError)):
        response = HttpResponse(status_code=error.status_code, body={
            'errors': [{
                'title': error.name,
                'detail': error.message
            }]
        })

        return response
    
    return HttpResponse(status_code=500, body={
        'errors': [{
            'title': 'Internal Server Error',
            'detail': 'An unexpected error occurred.'
        }]
    })