from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    return HttpResponse("Hello, World !")

def say_goodbye(request):
    return HttpResponse("So long World !")
