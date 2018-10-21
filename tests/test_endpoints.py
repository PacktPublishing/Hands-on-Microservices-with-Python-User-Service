from unittest import TestCase

import requests


class TestFlaskApiUsingRequests(TestCase):
    def test_login(self):
        response = requests.post('http://192.168.99.100:8082/api/login')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = requests.post('http://192.168.99.100:8082/api/user/logout')
        self.assertEqual(response.status_code, 200)