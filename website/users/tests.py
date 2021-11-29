from unittest.loader import TestLoader
from django.test import TestCase
from users.forms import CountryForm
from http import HTTPStatus
# Create your tests here.


class CountryFormTest(TestCase):
    def test_init(self):
        form = CountryForm(data={'country': 'Singapore'})
        print("form is ", form)
        # self.assertEqual(form.e)

    def test_get(self):
        response = self.client.get('/generate-report')
        self.assertEqual(response.status_code, HTTPStatus.OK)
