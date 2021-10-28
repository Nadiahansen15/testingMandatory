from django.test import TestCase
from .models import cellphone


class ModelTesting(TestCase):

    def setUp(self):
        self.cellphone = cellphone.objects.create(
            cellphone="Kussomaten",
            price=4000)

    def test_post_model(self):
        data = self.cellphone
        self.assertTrue(isinstance(data, cellphone))
        self.assertEqual(str(data), "Kussomaten")
