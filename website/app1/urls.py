
from django.urls import path
from .views import home, contact, services

urlpatterns = [
    path('', home, name="home"),
    path('contact', contact, name="contact"),
    path('services', services, name="services")
]