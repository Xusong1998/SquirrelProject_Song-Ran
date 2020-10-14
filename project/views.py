from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

def index(request):
    return render(request, 'project/home_page.html',{})

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
            'sightings': squirrels,
            }
    
    return render(request, 'project/map.html',context)
# Create your views here.
