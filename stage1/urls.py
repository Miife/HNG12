from django.urls import path
from .views import number_properties_api

urlpatterns = [
    path('number-properties/', number_properties_api, name='number-properties'),
]
