# api/blueprints/course.py

from flask import Blueprint, Response, json, request, g

from api.blueprints import custom_response
from api.models import Course, CourseSchema

courses_api = Blueprint('courses_api', __name__)
courses_schema = CourseSchema()


@courses_api.route('/', methods=['GET'])
def get_all():
    courses = Course.get_all_courses()
    data = courses_schema.dump(courses, many=True).data
    return custom_response(data, 200)


@courses_api.route('/', methods=['POST'])
def post_course():
    req_data = request.get_json()
    # req_data['course'] = g.user.get('id')
    data, error = courses_schema.load(req_data)
    if error:
        return custom_response(error, 400)
    course = Course(data)
    course.save()
    data = courses_schema.dump(course).data
    return custom_response(data, 200)


