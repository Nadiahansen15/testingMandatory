from django.contrib import admin
from .models import keaNet
from django import forms
from cellphone.models import cellphone, cellphoneForm


# Register your models here.

class SystemAdmin(admin.ModelAdmin):
    form = cellphoneForm
    filter_horizontal = ['cellphone',]

admin.site.register(keaNet)
