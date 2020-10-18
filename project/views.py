from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Squirrel
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .forms import AddSightingsForm
from .forms import UpdateForm

def index(request):
    return render(request, 'project/home_page.html',{})

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
            'sightings': squirrels,
            }
    return render(request, 'project/map.html',context)

def sightings(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }

    return render(request, 'project/sightings.html',context)


def detail(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    form = UpdateForm(instance = squirrel)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings')

    context = {
            'squirrel':  squirrel,
            'form': form,
            }

    return render(request, 'project/detail.html',context)

def stat(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }
            
    return render(request, 'project/stat.html', context)

def add(request):
    if request.method == 'POST':
        form = AddSightingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
        else:
            return JsonResponse({'errors': form.errors}, status = 400)
    return render(request, 'project/add.html', {})


def showthis(request):
    Squirrel.objects.all().delete()
    context()
    return render(request, 'project/home.html', context)
