
from django.test import TestCase
from cellphone.models import cellphone
from keaNet.models import keaNet
from django.utils import timezone


class testModels(TestCase):
    # before tests are run
    def setUp(self):
        self.cellphone = cellphone.objects.create(
            cellphone="Kussomaten",
            price=4000)

        self.keaNet = keaNet.objects.create(
            InternetConnection=True,
            PhoneLines=2,
            cellphone=self.cellphone,
            totalPrice=0,
            created_at=timezone.now()
        )

        self.keaNet1 = keaNet.objects.create(
            InternetConnection=False,
            PhoneLines=3,
            cellphone=self.cellphone,
            totalPrice=0,
            created_at=timezone.now()
        )

    def test_cellphone_model(self):
        data = self.cellphone
        self.assertTrue(isinstance(data, cellphone))
        self.assertEqual(str(data), "Kussomaten")

# test for edit of price
    def test_totalprice_can_be_new_price(self):
        data = self.keaNet
        if (data.InternetConnection == True):
            Connection = 200
        data.totalPrice = (data.PhoneLines*150) + data.cellphone.price + Connection
        self.assertTrue(isinstance(data, keaNet))
        self.assertEqual(str(data), ("True 2 Kussomaten 4500"))

    def test_internetConnection_add_to_price(self):
        data = self.keaNet
        if (data.InternetConnection == True):
            Connection = 200
        data.totalPrice = + data.totalPrice + Connection
        self.assertTrue(isinstance(data, keaNet))
        self.assertEqual(data.totalPrice, 200)

    def test_internetConnection_noAdd_to_price(self):
        data = self.keaNet1
        if (data.InternetConnection == False):
            connection = 0
        data.totalPrice = + connection
        self.assertEqual(data.totalPrice, 0)

    def test_count_of_phonelines(self):
        data = self.keaNet1
        data.totalPrice = +(data.PhoneLines*150)
        self.assertEqual(data.totalPrice, 450)
