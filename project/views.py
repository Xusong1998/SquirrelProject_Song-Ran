from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hi this is our homepage!')

# Create your views here.
