from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. Index")


# Handle Greetings
def greeting(request):
    return HttpResponse("")