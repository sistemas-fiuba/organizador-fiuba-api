# api/blueprints/professor.py

from flask import Blueprint, Response, json, request, g

from api.blueprints import custom_response
from api.models.professor import ProfessorSchema, Professor

professors_api = Blueprint('professors_api', __name__)
professors_schema = ProfessorSchema()


@professors_api.route('/', methods=['POST'])
def create():
    req_data = request.get_json()
    # req_data['professor'] = g.user.get('id')
    data, error = professors_schema.load(req_data)
    if error:
        return custom_response(error, 400)
    professor = Professor(data)
    professor.save()
    return custom_response(professor.id, 201)
