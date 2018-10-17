from flask import Blueprint, Response, json

from api.models import Course, CourseSchema

courses_api = Blueprint('courses_api', __name__)
courses_schema = CourseSchema()


@courses_api.route('/', methods=['GET'])
def get_all():
    courses = Course.get_all_courses()
    data = courses_schema.dump(courses, many=True).data
    return custom_response(data, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
