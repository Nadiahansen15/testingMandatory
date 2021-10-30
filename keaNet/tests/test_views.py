from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from keaNet.models import keaNet
from cellphone.models import cellphone
import json
from django.utils import timezone
from keaNet.views import keaNetView, keaNetFormView

class TestViews(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/keanetoverview/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('keanetoverview'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('keanetoverview'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'keaNet/keanetoverview.html')
    
    def test_keaNet_create_post(self):
        url = reverse('createkeaNet')
        response = self.client.post(url, {
            'InternetConnection': "True",
            'PhoneLines': "2",
            'cellphone': 'iPhone 99',
            'totalPrice': "6500",
            'created_at': timezone.now(),
        })
        self.assertEqual(response.status_code, 200)

