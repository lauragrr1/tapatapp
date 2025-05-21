import unittest
from server3 import app

class TestLoginEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_valid_user(self):
        response = self.app.post('/login', json={
            "username": "mare",
            "password": "12345"
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["username"], "mare")
        self.assertEqual(data["email"], "prova@gmail.com")
        self.assertEqual(data["token"], "token12345")
        self.assertEqual(data["idrole"], 2)
        self.assertEqual(data["msg"], "Usuari Ok")
        self.assertEqual(data["coderesponse"], "1")

    def test_login_invalid_user(self):
        response = self.app.post('/login', json={
            "username": "invalid_user",
            "password": "wrong_password"
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data["coderesponse"], "0")
        self.assertEqual(data["msg"], "No validat")

    def test_login_valid_token(self):
        response = self.app.post('/login', headers={
            "Authorization": "Bearer token12345"
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["username"], "mare")
        self.assertEqual(data["email"], "prova@gmail.com")
        self.assertEqual(data["token"], "token12345")
        self.assertEqual(data["idrole"], 2)
        self.assertEqual(data["msg"], "Usuari Ok")
        self.assertEqual(data["coderesponse"], "1")

    def test_login_invalid_token(self):
        response = self.app.post('/login', headers={
            "Authorization": "Bearer invalid_token"
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data["coderesponse"], "0")
        self.assertEqual(data["msg"], "No validat")

if __name__ == '__main__':
    unittest.main()