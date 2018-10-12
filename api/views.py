from flask import jsonify

from api import app


@app.route('/', methods=['GET'])
def not_a_teapot():
    return "I'm not a teapot"


@app.route('/api', methods=['GET'])
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
