from django.test import TestCase
from django.urls import reverse


class JsonRpcViewTests(TestCase):
    def test_valid_form_submission(self):
        url = reverse('jsonrpc-form')
        data = {
            'method': 'some_method',
            'params': '{"key": "value"}',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.context)

    def test_invalid_json_submission(self):
        url = reverse('jsonrpc-form')
        data = {
            'method': 'some_method',
            'params': 'invalid_json',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.context)
        self.assertIn('Invalid JSON', response.context['result'])
