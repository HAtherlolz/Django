from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import *
import json

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
# Create your views here.


class ServMonView(ListView):
    '''Полный список'''
    model = ServMonitor
    queryset = ServMonitor.objects.filter(draft=False)

class ServDetail(DetailView):
    '''Таргетно'''
    model = ServMonitor
    slug_field = "url"


def export(request):
    bd = ServMonitor.objects.filter(url=slug)
    for i in bd:
        data = {'name': i.name, 'type': i.type, 'email': i.email, 'group': i.group, 'group_type': i.group_type, 'gps': i.gps, 'url': i.url}
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="members.json"'
    return response


class ServCreateView(CreateView):
    model = ServMonitor
    fields = ('name', 'time', 'type', 'email', 'group', 'group_type', 'gps', 'url')


'''PDF'''
class PdfMakerList(ListView):
    model = PdfMaker
    queryset = ServMonitor.objects.all()
    template = 'comments\pdfmaker_list.html'

class PdfMakerDetail(DetailView):
    model = PdfMaker
    slug_field = "url"


class PdfMakerCreateView(CreateView):
    model = PdfMaker
    fields = ('name', 'time', 'type', 'email', 'url')


def pdf_export(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    bd = PdfMaker.objects.all()
    for i in bd:
        p.drawString(100, 100, i.name)
        #p.drawString(100, 150, i.time)
        p.drawString(100, 200, i.type)
        p.drawString(100, 250, i.email)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
