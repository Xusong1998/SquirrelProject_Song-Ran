from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'project'

urlpatterns = [
        path('', views.index),
        path('map', views.map),
        path('sightings', views.sightings),

        path('sightings/<int:squirrel_id>/', views.detail, name='detail'),
        
        path('sightings/add', views.add, name = 'add'),
        path('sightings/stats', views.stat)]



