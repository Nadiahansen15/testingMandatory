from django.db import models
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator
from cellphone.models import cellphone


# Create your models here.
class keaNet(models.Model):
    InternetConnection = models.BooleanField()
    PhoneLines = models.IntegerField(validators=[MaxValueValidator(8), MinValueValidator(0)])
    cellphone = models.ForeignKey(cellphone, on_delete=models.CASCADE, default=None)
    totalPrice = models.FloatField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.InternetConnection, self.PhoneLines, self.cellphone, self.totalPrice)


class keaNetForm(ModelForm):
    def init(self, args, **kwargs):
        super(keaNetForm, self).__init__(args, **kwargs)

    class Meta:
        model = keaNet
        fields = '__all__'
        exclude = ['totalPrice', 'created_at']
        labels = {
            "InternetConnection": ("Internet connection"),
            "PhoneLines": ("Phone Lines"),
            "cellphone": ("cell Phones"),
        }
