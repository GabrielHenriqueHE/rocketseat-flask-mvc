from flask import Flask
from flask_cors import CORS

from src.main.routes.pet_route import pet_route_bp
from src.main.routes.person_routes import person_route_bp
from src.models.sqlite.settings.connection import DBConnectionHandler

connection_handler = DBConnectionHandler()
connection_handler.connect()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pet_route_bp)
app.register_blueprint(person_route_bp)