from django.db import models
from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator
from cellphone.models import cellphone
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from django.contrib import admin


# Create your models here.
class keaNet(models.Model):
    InternetConnection = models.BooleanField()
    PhoneLines = models.IntegerField(validators=[MaxValueValidator(8)])
    cellphone = models.ManyToManyField(cellphone)
    FilteredSelectMultiple
    totalPrice = models.FloatField()

def __str__(self):
    return '{} {} {} {}'.format(self.InternetConnection, self.PhoneLines, self.cellphone, self.totalPrice)

class keaNetForm(forms.ModelForm):
    def init(self, args, **kwargs):
            super(keaNetForm, self).__init__(args, **kwargs)

    class Meta:
        model = keaNet
        # exclude = ('totalprice')
        fields = '__all__'
        labels = {
            "InternetConnection": ("Internet connection"),
            "PhoneLines": ("Phone Lines"),
            "cellphone": ("cell Phones"),
            "totalPrice": ("Total Price"),
        }
