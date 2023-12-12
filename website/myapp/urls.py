
from django.urls import path
from .views import home, contact, service, upload_image

urlpatterns = [
    path("", home),
    path("myapp/v1/contact", contact),
    path("myapp/v1/service", service),
    path("upload_image", upload_image, name="upload_image")
]