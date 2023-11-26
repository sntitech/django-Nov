from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Person
from .utils import send_mail_to_user
from datetime import date

@api_view(['GET'])
def ping(request):
    return HttpResponse("Service up and running...")


@api_view(['GET'])
def index(request):
    today = date.today()
    b_obj = Book.objects.filter(pk = id)
    if Book:
        b_obj.end_date < today:
            
    persons = Person.objects.all().values()
    if len(persons) == 0:
        res = "DATA NOT AVAILBALE."
    else:
        res = persons
    return HttpResponse(res)


@api_view(['POST'])
def create_person(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    is_active = True

    p_obj = Person.objects.create(first_name=first_name, last_name=last_name, email=email, is_active=is_active)
    p_obj.save()
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