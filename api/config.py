# /src/config.py


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = "postgres://postgres@localhost:5432/fiuba_organizer"
    BASE_URL = "http://localhost:5000"
    API = "/api/v1"
    VERSION_CODE = "1.0.0"


app_config = {
    'development': Development,
}
