from django.test import SimpleTestCase
from django.urls import reverse, resolve
from keaNet.views import keaNetView, keaNetFormView


class TestUrls(SimpleTestCase):
    def test_keanetoverview_url_is_resolved(self):
        url = reverse('keanetoverview')
        self.assertEquals(resolve(url).func.view_class, keaNetView)

    def test_keaNetFormView_url_is_resolved(self):
        url = reverse('createkeaNet')
        self.assertEquals(resolve(url).func.view_class, keaNetFormView)
