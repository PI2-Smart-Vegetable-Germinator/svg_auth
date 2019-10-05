from project.tests.base import BaseTestCase
from project.api.auth.models import Users


class SignupTest(BaseTestCase):
    def test_ping(self):
        response = self.client.get('/api/ping')
        self.assert200(response)

    def test_register_with_correct_fields_creates_user(self):
        post_data = {
            'user': {
                'email': 'email@test.com',
                'password': 'somepassword'
            }
        }

        response = self.client.post('/api/signup', json=post_data)

        users = Users.query.all()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(users), 1)

    def test_register_fails_without_email(self):
        post_data = {
            'user': {
                'password': 'somepassowrd'
            }
        }

        response = self.client.post('/api/signup', json=post_data)

        users = Users.query.all()

        self.assert400(response)
        self.assertEqual(len(users), 0)

    def test_register_fails_without_password(self):
        post_data = {
            'user': {
                'email': 'some@email.com'
            }
        }

        response = self.client.post('/api/signup', json=post_data)

        users = Users.query.all()

        self.assert400(response)
        self.assertEqual(len(users), 0)


class LoginTest(BaseTestCase):
    def create_user(self):
        post_data = {
            'user': {
                'email': 'email@test.com',
                'password': 'somepassword'
            }
        }

        self.client.post('/api/signup', json=post_data)

    def test_login_works_with_valid_credentials(self):
        self.create_user()

        post_data = {
            'email': 'email@test.com',
            'password': 'somepassword',
        }

        response = self.client.post(
            '/api/login',
            json=(post_data)
        )

        response_data = response.json

        user = Users.query.first()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(user.id, response_data['userId'])

    def test_login_fails_with_wrong_email(self):
        self.create_user()

        post_data = {
            'email': 'email@wrong.com',
            'password': 'somepassword',
        }

        response = self.client.post(
            '/api/login',
            json=(post_data)
        )

        self.assert401(response)

    def test_login_fails_with_wrong_password(self):
        self.create_user()

        post_data = {
            'email': 'email@test.com',
            'password': 'somewrongpassword',
        }

        response = self.client.post(
            '/api/login',
            json=(post_data)
        )

        self.assert401(response)
