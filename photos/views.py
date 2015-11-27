from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from photos.models import Photo


def home(request):
    photos = Photo.objects.all()
    context = {
        'photos_list': photos[:5]
    }

    return render(request, 'photos/home.html', context)
