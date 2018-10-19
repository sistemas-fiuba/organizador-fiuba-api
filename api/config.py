# /src/config.py



class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/fiuba_organizer"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_URL = "http://localhost:5000"
    API = "/api/v1"
    VERSION_CODE = "1.0.0"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
