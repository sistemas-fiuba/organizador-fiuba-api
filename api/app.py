# api/app.py

from flask import Flask, jsonify

from .config import app_config
from .models import db

# import courses blueprint
from .blueprints.course import courses_api as courses_blueprint


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    config = app_config[env_name]
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    db.metadata.clear()

    app.register_blueprint(courses_blueprint, url_prefix=config.API + '/courses')

    @app.route('/', methods=['GET'])
    def not_a_teapot():
        return "I'm not a teapot"

    @app.route(config.API, methods=['GET'])
    def api_info():
        """Welcome message for the API."""
        # Message to the user
        message = {
            'name': 'Organizador de Cursos FIUBA',
            'apiVersion': 'v1.0',
            'status': '200',
            'message': 'Primera versión del Organizador de Cursos'
        }
        # Making the message looks good
        resp = jsonify(message)
        # Returning the object
        return resp

    return app
