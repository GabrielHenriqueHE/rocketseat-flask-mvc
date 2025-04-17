from flask import Blueprint, jsonify, request

from src.errors.error_handler import error_handler
from src.main.composer.person_creator_composer import person_creator_composer
from src.main.composer.person_finder_composer import person_finder_composer
from src.views.httptypes.http_request import HttpRequest

person_route_bp = Blueprint('person_route', __name__)

@person_route_bp.route('/people', methods=['POST'])
def create_person():
    try:
        view_request = HttpRequest(body=request.json)
        view = person_creator_composer()

        response = view.handle(view_request)

        return jsonify(response.body), response.status_code
    except Exception as e:
        response = error_handler(e)
        return jsonify(response.body), response.status_code


@person_route_bp.route('/people/<int:person_id>', methods=['GET'])
def get_person(person_id):
    try:
        view_request = HttpRequest(param={'person_id': person_id})
        view = person_finder_composer()

        response = view.handle(view_request)

        return jsonify(response.body), response.status_code
    except Exception as e:
        response = error_handler(e)
        return jsonify(response.body), response.status_code