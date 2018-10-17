# api/models/professor.py
import datetime

from marshmallow import fields, Schema
from api.models import db


class Professor(db.Model):
    """
    Professor Model
    """

    # table name
    __tablename__ = 'course'
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
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


class ProfessorSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
