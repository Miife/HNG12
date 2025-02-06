from django.urls import path
from .views import number_properties_api

urlpatterns = [
    path('classify-number/', number_properties_api, name='classify-number'),
]
