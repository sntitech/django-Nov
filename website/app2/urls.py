from django.urls import path
from .views import index, create_person, ping, mail, task, upload_image

urlpatterns = [
    path('ping', ping, name="ping"),
    path('', index, name="home"),
    path('createPerson', create_person, name="create_person"),
    path('mail', mail, name="send_mail_to_user"),
    path('task', task, name="task"),
    path('upload_image', upload_image, name="upload_image")
]