from flask import Blueprint, jsonify

from src.errors.error_handler import error_handler
from src.main.composer.pet_deleter_composer import pet_deleter_composer
from src.main.composer.pet_finder_composer import pet_finder_composer
from src.views.httptypes.http_request import HttpRequest

pet_route_bp = Blueprint('pet_route', __name__)

@pet_route_bp.route('/pets', methods=['GET'])
def get_pets():
    try:
        view_request = HttpRequest()
        view = pet_finder_composer()

        response = view.handle(view_request)

        return jsonify(response.body), response.status_code
    except Exception as e:
        response = error_handler(e)
        return jsonify(response.body), response.status_code

@pet_route_bp.route('/pets/<name>', methods=['DELETE'])
def delete_pet(name):
    try:
        view_request = HttpRequest(param={'name': name})
        
        view = pet_deleter_composer()

        response = view.handle(view_request)

        return jsonify(response.body), response.status_code
    except Exception as e:
        response = error_handler(e)
        return jsonify(response.body), response.status_code