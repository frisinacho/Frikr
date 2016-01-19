# -*- coding: utf-8 -*-
from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PhotoListAPI(ListCreateAPIView):
    queryset = Photo.objects.all()

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == "POST" else PhotoListSerializer


class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
