from django.urls import path
from .views import my_info

urlpatterns =[
    path('', my_info, name='my_info'),
]