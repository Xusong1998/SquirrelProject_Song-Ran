from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'project/home_page.html',{})

# Create your views here.
