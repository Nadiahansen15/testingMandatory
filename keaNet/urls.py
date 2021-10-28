from django.urls import path
from .views import keaNetView, keaNetFormView

urlpatterns = [
    path('keanetoverview/', keaNetView.as_view(), name="keanetoverview"),
    path('createkeaNet/', keaNetFormView.as_view(), name="createkeaNet"),
    # url(r'^ajax/cal_Total_Price/$', views.cal_Total_Price, name='cal_Total_Price'),
]
