# api/models/course.py
import datetime

from marshmallow import fields, Schema

from professor import ProfessorSchema
from api.models import db


class Course(db.Model):
    """
      Course Model
      """

    # table name
    __tablename__ = 'course'
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, nullable=False)
    classroom = db.Column(db.String(128), nullable=False)
    day = db.Column(db.String(128), nullable=False)
    time = db.Column(db.String(128), nullable=False)
    professor_id = db.Column(db.Integer, nullable=False)
    # professors = db.relationship('Professor', backref='course', lazy=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_one_course(id):
        return Course.query.get(id)

    @staticmethod
    def get_all_courses():
        return Course.query.all()

class CourseSchema(Schema):
    id = fields.Int(dump_only=True)
    subject_id = fields.Int(required=True)
    classroom = fields.Str(required=True)
    professor_id = fields.Int(required=True)
    # professors = fields.Nested(ProfessorSchema, many=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
