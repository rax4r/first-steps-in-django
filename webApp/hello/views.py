from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello, World!")

def nikita(request):
    return HttpResponse("Hello, nikita")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })