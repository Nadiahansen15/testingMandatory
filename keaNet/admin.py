from django.contrib import admin
from .models import keaNet
from cellphone.models import cellphoneForm


# Register your models here.

class SystemAdmin(admin.ModelAdmin):
    form = cellphoneForm
    filter_horizontal = ['cellphone', ]


admin.site.register(keaNet)
