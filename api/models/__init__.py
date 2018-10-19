# src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# initialize our db

db = SQLAlchemy()


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True
    # define here __repr__ and json methods or any common method
    # that you need for all your models


from .professor import Professor, ProfessorSchema
from .course import Course, CourseSchema
