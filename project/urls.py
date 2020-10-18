from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'project'

urlpatterns = [
        path('', views.index, name = 'index'),
        path('map', views.map, name = 'map'),
        path('sightings', views.sightings, name = 'sightings'),

        path('sightings/<str:Unique_Squirrel_ID>/', views.detail, name='detail'),     
        path('sightings/add', views.add, name = 'add'),
        path('sightings/stats', views.stat, name = 'stats'),
        ]


