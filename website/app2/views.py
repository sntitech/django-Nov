from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Person, Task
from .utils import send_mail_to_user
from django.http import JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from django.db import connection

with connection.cursor() as cursor:
    # Replace 'your_stored_procedure' with the actual name of your stored procedure
    cursor.execute('SELECT * FROM get_productss();')
    # If your stored procedure returns a result set, fetch the results
    results = cursor.fetchall()
    print(results)
    


@api_view(['GET'])
def ping(request):
    return HttpResponse("Service up and running...")


@api_view(['GET'])
def index(request):            
    # persons = Person.objects.all().values()
    # if len(persons) == 0:
    #     res = "DATA NOT AVAILBALE."
    # else:
    #     res = persons
    # return HttpResponse(res)
    return render(request, "home.html")


@api_view(['GET','POST'])
def task(request):
    if request.method == "GET":
        tasks = Task.objects.all().values()
        return HttpResponse(tasks)
    else:
        print("task id===", request.data.get('task_id'))
        task_id = request.data.get('task_id')
        task = Task.objects.get(id=task_id)
        task_obj = {
            "name": task.name,
            "personFirstName": task.person.first_name,
            "personLastName": task.person.last_name,
            "personEmail": task.person.email
        }

        return JsonResponse(task_obj)


@api_view(['POST'])
def create_person(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    is_active = True

    p_obj = Person.objects.create(first_name=first_name, last_name=last_name, email=email, is_active=is_active)
    p_obj.save()

    t_obj = Task.objects.create(name=request.data.get('task_name'), person=p_obj)
    t_obj.save()
    # result = send_mail_to_user(first_name, last_name, email)
    # print(result)
    return HttpResponse("Person Successfully Added.")


@api_view(['POST'])
def mail(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    send_mail_to_user(first_name, last_name, email)
    return HttpResponse("Mail Send.")

import cloudinary
import cloudinary.uploader
import cloudinary.api

CLOUDINARY_URL="cloudinary://511947514892351:uE0AXqO3Z3KUDuc10WDaN4_fE38@damyuborr"

CLOUDINARY_URL="cloudinary://511947514892351:uE0AXqO3Z3KUDuc10WDaN4_fE38@damyuborr?cname=mydomain.com&upload_prefix=myprefix.com"

@api_view(['POST'])
def upload_image(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print("MYFILE IS HERE---->>>>", myfile)
        
    #     fs = FileSystemStorage()
    #     filename = fs.save(myfile.name, myfile)
    #     uploaded_file_url = fs.url(filename)
    #     return render(request, 'core/simple_upload.html', {
    #         'uploaded_file_url': uploaded_file_url
    #     })
    # return render(request, 'core/simple_upload.html')
        cloudinary.config( 
        cloud_name = "damyuborr", 
        api_key = "511947514892351", 
        api_secret = "uE0AXqO3Z3KUDuc10WDaN4_fE38" 
        )
        # result = cloudinary.uploader.upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg", public_id = "olympic_flag")
        result = cloudinary.uploader.upload(
        myfile,
        folder="",
        resource_type="image", public_id = "mynature")
        print("Result is here--->>>", result)
        return HttpResponse("File Uploded..")


# upload_image()

def get_image_info():
    cloudinary.config( 
    cloud_name = "damyuborr", 
    api_key = "511947514892351", 
    api_secret = "uE0AXqO3Z3KUDuc10WDaN4_fE38" 
    )
    result = cloudinary.api.resource_by_asset_id("514d03c014347b375cd97198cf12556a")
    print(result)

# get_image_info()