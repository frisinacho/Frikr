# -*- coding: utf-8 -*-
from photos.models import Photo
from photos.serializers import PhotoSerializer
from rest_framework.generics import ListCreateAPIView


class PhotoListAPI(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
