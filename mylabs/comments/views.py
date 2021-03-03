from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import *
# Create your views here.

class ServMonView(ListView):
    '''Список фильмов'''
    model = ServMonitor
    queryset = ServMonitor.objects.filter(draft=False)

class ServCreateView(CreateView):
    model = ServMonitor
    fields = ('name', 'time', 'type', 'email', 'group', 'group_type', 'gps', 'url')
