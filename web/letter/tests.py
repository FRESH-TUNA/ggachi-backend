from django.test import TestCase
from django.db import models
from django.test import Client
import json

from ggachiauth.models import User
from letter.models import Letter

class CreateLetterTest(TestCase):
    def setUp(self):
        User.objects.create_user(email="root@gmail.com", password="1234")

    def test_with_account(self):
        c = Client()

        response = c.post(
            '/api/letters', 
            json.dumps({
                'bride': 'bride',
                'groom': 'groom',
                'place_name': 'place_name',
                'place_address': 'place_address',
                'start_time': 'start_time',
                'howtobus': 'howtobus',
                'howtosubway': 'howtosubway',
                'message': 'message',
                'template': 1,
                'email': 'root@gmail.com',
                'password1': '1234',
                'password2': '1234'
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 1) 
        self.assertEqual(response.data['message'], 'message')

    def test_without_account(self):
        c = Client()

        response = c.post(
            '/api/letters', 
            json.dumps({
                'bride': 'bride',
                'groom': 'groom',
                'place_name': 'place_name',
                'place_address': 'place_address',
                'start_time': 'start_time',
                'howtobus': 'howtobus',
                'howtosubway': 'howtosubway',
                'message': 'message2',
                'template': 1,
                'email': 'rove@gmail.com',
                'password1': '1234',
                'password2': '1234'
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 2) 
        self.assertEqual(response.data['message'], 'message2')


class RetrieveLetterTest(TestCase):
    def setUp(self):
        c = Client()
        User.objects.create_user(email="root@gmail.com", password="1234")
        response = c.post(
            '/api/letters', 
            json.dumps({
                'bride': 'bride1',
                'groom': 'groom',
                'place_name': 'place_name',
                'place_address': 'place_address',
                'start_time': 'start_time',
                'howtobus': 'howtobus',
                'howtosubway': 'howtosubway',
                'message': 'message2',
                'template': 1,
                'email': 'rove@gmail.com',
                'password1': '1234',
                'password2': '1234'
            }),
            content_type="application/json"
        )
        response = c.post(
            '/api/letters', 
            json.dumps({
                'bride': 'bride2',
                'groom': 'groom',
                'place_name': 'place_name',
                'place_address': 'place_address',
                'start_time': 'start_time',
                'howtobus': 'howtobus',
                'howtosubway': 'howtosubway',
                'message': 'message2',
                'template': 1,
                'email': 'rove@gmail.com',
                'password1': '1234',
                'password2': '1234'
            }),
            content_type="application/json"
        )

    def test_retrieve(self):
        c = Client()
        response = c.get('/api/letters/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 3) 
        self.assertEqual(response.data['bride'], 'bride1')

        response = c.get('/api/letters/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 4) 
        self.assertEqual(response.data['bride'], 'bride2')

class ListLetterTest(TestCase):
    def setUp(self):
        c = Client()
        User.objects.create_user(email="root@gmail.com", password="1234")
        response = c.post(
            '/api/letters', 
            json.dumps({
                'bride': 'bride1',
                'groom': 'groom',
                'place_name': 'place_name',
                'place_address': 'place_address',
                'start_time': 'start_time',
                'howtobus': 'howtobus',
                'howtosubway': 'howtosubway',
                'message': 'message2',
                'template': 1,
                'email': 'root@gmail.com',
                'password1': '1234',
                'password2': '1234'
            }),
            content_type="application/json"
        )
        response = c.post(
            '/api/letters', 
            json.dumps({
                'bride': 'bride2',
                'groom': 'groom',
                'place_name': 'place_name',
                'place_address': 'place_address',
                'start_time': 'start_time',
                'howtobus': 'howtobus',
                'howtosubway': 'howtosubway',
                'message': 'message2',
                'template': 1,
                'email': 'root@gmail.com',
                'password1': '1234',
                'password2': '1234'
            }),
            content_type="application/json"
        )

    def test_list(self):
        c = Client()
        response = c.post(
            '/api/letters/mine', 
            json.dumps({
                'email': 'root@gmail.com',
                'password': '1234'
            }),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2) 