from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app1.models import Person, Student
import requests, json
from app1.utils import convert_request_body_into_json

@csrf_exempt
def home(request):
    if request.method == 'GET':
        p_data = Person.objects.all().values()
        return HttpResponse(p_data, content_type="application/json")
    elif request.method == 'POST':
        request_body = convert_request_body_into_json(request.body)
        p_obj = Person(first_name = request_body.get('first_name'), 
                       last_name = request_body.get('last_name'),
                       city = request_body.get('city'),
                       subject = request_body.get('subject')
                       )
        p_obj.save()
        return HttpResponse("Data Successfully Saved.")


def contact(request):
    if request.method == 'POST':
        return render(request, "contact.html")

def services(request):
    return render(request, "services.html")
