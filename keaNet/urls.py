from django.urls import path
from .views import keaNetView, keaNetFormView

urlpatterns = [
    path('keanetoverview/', keaNetView.as_view(), name="keanetoverview"),
    path('createkeaNet/', keaNetFormView.as_view(), name="createkeaNet"),
]
