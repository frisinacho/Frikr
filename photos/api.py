# -*- coding: utf-8 -*-
from photos.models import Photo
from photos.serializers import PhotoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class PhotoListAPI(APIView):

    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)
