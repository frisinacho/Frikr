# -*- coding: utf-8 -*-
from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotosQuerySet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet


class PhotoViewSet(PhotosQuerySet, ModelViewSet):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description', 'owner__first_name')
    ordering_fields = ('name', 'owner')

    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def get_serializer_class(self):
        """
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer
        """
        return PhotoListSerializer if self.action == 'list' else PhotoSerializer

    def perform_create(self, serializer):
        """
        Asigna automáticamente la autoría de la nueva foto
        al usuario autenticado
        """
        serializer.save(owner=self.request.user)
