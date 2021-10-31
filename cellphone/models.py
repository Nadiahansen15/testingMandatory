from django.db import models
from django.forms import ModelForm

# Create your models here.


class cellphone(models.Model):
    cellphone = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.cellphone


class cellphoneForm(ModelForm):
    def init(self, args, **kwargs):
        super(cellphoneForm, self).__init__(args, **kwargs)

    class Meta:
        model = cellphone
        fields = '__all__'
