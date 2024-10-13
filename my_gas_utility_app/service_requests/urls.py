from django.urls import path
from .views import submit_service_request

urlpatterns = [
    path('submit/', submit_service_request, name='submit_service_request'),
]
