# api/app.py
import os

from flask_sqlalchemy import SQLAlchemy
from healthcheck import HealthCheck
from flask import Flask, jsonify

# from .config import app_config

from api.config import app_config
from .models import db
from .blueprints.course import courses_api as courses_blueprint
from .blueprints.professor import professors_api as professors_blueprint


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    config = app_config[env_name if env_name else os.getenv('FLASK_ENV')]
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    # app.config['SQLALCHEMY_DATABASE_URI'] =

    app.register_blueprint(courses_blueprint, url_prefix=config.API + '/courses')
    app.register_blueprint(professors_blueprint, url_prefix=config.API + '/professors')

    @app.before_first_request
    def create_data():
        db.create_all()

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

    # wrap the flask app and give a heathcheck url
    health = HealthCheck(app, "/healthcheck")

    def health_database_status():
        is_database_working = True
        output = 'database is ok'

        try:
            # to check database we will execute raw query
            # db.create_all()
            db.session.execute('SELECT 1')
        except Exception as e:
            output = str(e)
            is_database_working = False

        return is_database_working, output

    health.add_check(health_database_status)
    return app
