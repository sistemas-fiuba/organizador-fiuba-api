#  test/01_professor_test.py

import unittest

from flask import json

from api.app import create_app
from api.models import Course, Professor, db


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        """
        Test Setup
        """
        self.app = create_app("development")
        self.client = self.app.test_client
        self.professor = {
            'name': 'Acero, Fernando'
        }

        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_user_creation(self):
        """ test user creation with valid credentials """
        res = self.client().post('/api/v1/professors/', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.professor))
        # json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)

    def test_get(self):
        self.assertIsNotNone(Professor.query.get(1))

    def test_save(self):
        professor = Professor({'name': "Profesor de prueba"})
        self.assertIsNotNone(professor)
        professor.save()
