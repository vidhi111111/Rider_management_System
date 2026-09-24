from flask import Flask
from flask_cors import CORS

from .routes import register_routes


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
    register_routes(app)
    return app
