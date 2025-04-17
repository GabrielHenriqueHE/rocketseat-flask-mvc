from flask import Blueprint, jsonify

from src.main.composer.pet_deleter_composer import pet_deleter_composer
from src.main.composer.pet_finder_composer import pet_finder_composer
from src.views.httptypes.http_request import HttpRequest

pet_route_bp = Blueprint('pet_route', __name__)

@pet_route_bp.route('/pets', methods=['GET'])
def get_pets():
    view_request = HttpRequest()
    view = pet_finder_composer()

    response = view.handle(view_request)

    return jsonify(response.body), response.status_code

@pet_route_bp.route('/pets/<name>', methods=['DELETE'])
def delete_pet(name):
    view_request = HttpRequest(param={'name': name})
    
    view = pet_deleter_composer()

    response = view.handle(view_request)

    return jsonify(response.body), response.status_code