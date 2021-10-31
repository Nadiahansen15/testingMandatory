from django.test import TestCase
from django.utils import timezone
from keaNet.models import keaNetForm, keaNet
from cellphone.models import cellphone


class TestForms(TestCase):
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
# tests that form is valid with data

    def test_keaNet_form_valid_data(self):
        form = keaNetForm(data={
            'InternetConnection': True,
            'PhoneLines': 2,
            'cellphone': self.cellphone,
            'totalPrice': 0,
            'created_at': timezone.now()
        })
        self.assertTrue(form.is_valid())

    def test_keaNet_form_unvalid_data(self):
        form = keaNetForm(data={
            'InternetConnection': "string",
            'PhoneLines': 9,
            'cellphone': self.cellphone,
            'totalPrice': '6500',
            'created_at': timezone.now()
        })
        self.assertFalse(form.is_valid())

# tests form fails if no data
    def test_keaNet_form_no_data(self):
        form = keaNetForm(data={})
        self.assertFalse(form.is_valid())

# test the labels are correct
    def test_keaNet_internetconnection_label(self):
        form = keaNetForm()
        self.assertTrue(form.fields['InternetConnection'].label == 'Internet connection')

    def test_keaNet_PhoneLines_label(self):
        form = keaNetForm()
        self.assertTrue(form.fields['PhoneLines'].label == 'Phone Lines')

    def test_keaNet_cellphone_label(self):
        form = keaNetForm()
        self.assertTrue(form.fields['cellphone'].label == 'cell Phones')

    # def test_new_price_for_adding_item(self):
        # form = keaNetForm()
