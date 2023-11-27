from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Person, Task
from .utils import send_mail_to_user
from django.http import JsonResponse


@api_view(['GET'])
def ping(request):
    return HttpResponse("Service up and running...")


@api_view(['GET'])
def index(request):            
    persons = Person.objects.all().values()
    if len(persons) == 0:
        res = "DATA NOT AVAILBALE."
    else:
        res = persons
    return HttpResponse(res)


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

