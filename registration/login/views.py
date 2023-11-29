from django.shortcuts import render, redirect
from .models import Register
from django.core.serializers import serialize
import json


def home(request):
    return render(request, "home.html")


def login(request):
    if request.method == "POST":
        reg_obj = Register.objects.filter(email = request.POST.get('email'), password=request.POST.get('password'))
        if reg_obj:
            context = serialize("json", reg_obj)
            context = json.loads(context) 
            name = "".join([f"{obj.get('fields').get('first_name')} {obj.get('fields').get('last_name')}" for obj in context])
            res = {
                "name": name
            }
            return render(request, "landing.html", context=res)
        else:
            return redirect('login')
    
    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        if request.POST.get('username'):
            first_name = request.POST.get('username').split(' ')[0]
            last_name = request.POST.get('username').split(' ')[1]
        register = Register.objects.create(first_name=first_name, last_name=last_name, email = request.POST.get('email'), password=request.POST.get('password'))
        register.save()
        print("SIGN UP SUCCESS")
        return redirect('login')
        
    return render(request, "signup.html")
