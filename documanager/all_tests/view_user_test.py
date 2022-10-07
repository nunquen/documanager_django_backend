from django.test import TestCase
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase
from typing import Tuple
from typing import List

def get_all_users() -> List[Tuple]:
    users = [
        (1,"Gemma", "Propylon2022"),
        (2,"Brendan", "Propylon2022"),
        (3,"Saul", "Propylon2022")
    ]
    return users

def get_unknown_user() -> List[Tuple]:
    return [(0,"Unknown", "any_text")]

class UserTest(APITestCase):
    @parameterized.expand(get_all_users())
    def test_retrieve_all_users(self, id, name, password):
        response = self.client.get('/v1/users/')
        """ Checking OK response """
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """ Checking that all users exists """
        res = next((sub for sub in response.data if sub['name'] == name), None)
        self.assertNotEqual(res, None)
        self.assertEqual(password, res["password"])
        
    @parameterized.expand(get_all_users())
    def test_retrieve_single_user(self, id, name, password):
        response = self.client.get('/v1/user/{}'.format(id))
        """ Checking OK response """
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """ Checking id, name and password """
        self.assertEqual(id, response.data["id"])
        self.assertEqual(name, response.data["name"])
        self.assertEqual(password, response.data["password"])

    @parameterized.expand(get_unknown_user())
    def test_retrieve_single_user(self, id, name, password):
        response = self.client.get('/v1/user/{}'.format(id))
        """ Checking OK response """
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
