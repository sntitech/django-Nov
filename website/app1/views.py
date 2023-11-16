from django.shortcuts import render
import requests

def home(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response_obj = {
        "users": response.json()
    }
    return render(request, "home.html", context=response_obj)

def contact(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")
