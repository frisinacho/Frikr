from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from photos.models import Photo


def home(request):
    photos = Photo.objects.all()
    html = '<ul>'
    html += '</ul>'
    return HttpResponse("Hola mundo!")
