from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import keaNetView, keaNetFormView
from . import views

urlpatterns = [
    path('keanetoverview/', keaNetView.as_view(), name = "keanetoverview"),
    path('createkeaNet/', keaNetFormView.as_view(), name = "createkeaNet"),
    # url(r'^ajax/cal_Total_Price/$', views.cal_Total_Price, name='cal_Total_Price'),
]
