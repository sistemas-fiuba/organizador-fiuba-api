# api/blueprints/__init__.py
from flask import Response, json


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )


from api.blueprints import *
