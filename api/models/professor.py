# api/models/professor.py
import datetime

from marshmallow import fields, Schema
from api.models import db, BaseModel


class Professor(BaseModel):
    """
    Professor Model
    """

    # table name
    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    modified_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, data):
        # self.id = data.get('id')
        self.name = data.get('name')

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
    name = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
