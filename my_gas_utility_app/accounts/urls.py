from django.urls import path
from .views import register_customer
from .views import home

urlpatterns = [
    path('register/', register_customer, name='register_customer'),
    path('', home, name='home'),  
]
