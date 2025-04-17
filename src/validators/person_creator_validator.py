from pydantic import BaseModel, constr, ValidationError

from src.errors.errortypes.http_unprocessable_entity import HttpUnprocessableEntityError
from src.views.httptypes.http_request import HttpRequest

def person_creator_validator(request: HttpRequest) -> None:
    class BodyData(BaseModel):
        first_name: constr(min_length=1)
        last_name: constr(min_length=1)
        age: int
        pet_id: int

    try:
        BodyData(**request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors())