from app import app
import unittest
from flask import url_for


class ApiTestCase(unittest.TestCase):

    def test_no_auth(self):
        tester = app.test_client(self)
        response = tester.get(url_for('app.get_tasks'), content_type='application/json')
        self.assertTrue(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
