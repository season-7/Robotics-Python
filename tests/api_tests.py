from app import app
import json
import unittest
from flask import url_for, current_app, redirect


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_no_auth(self):
        response = self.app.get('/pi/app/tasks', content_type='application/json')
        self.assertTrue(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
