# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from photos.models import Photo, PUBLIC


def home(request):
    """
    Esta función devuelve el home de mi página
    """
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list': photos[:5]
    }

    return render(request, 'photos/home.html', context)


def detail(request, pk):
    """
    Carga la página de detalle de una foto
    :param request: HttpRequest
    :param pk: id de la foto
    :return: HttpResponse
    """
    """
    También se puede utilizar esta sintaxis de recuperación de un objeto:
    try:
        photo = Photo.object.het(pk=pk)
    except Photo.DoesNotExist:
        photo = None
    except Photo.MultipleObjects:
        photo = None
    """
    possible_photos = Photo.object.filter(pk=pk)
    # JS: photo = (possible_photo.length == 1) ? possible_photo[0] : null;
    photo = possible_photos[0] if len(possible_photos) == 1 else None
    if photo is not None:
        # cargar plantilla detalle
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound()   # 404 not found
