# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        read_only_fields =('owner',)


class PhotoListSerializer(PhotoSerializer):

    class Meta(PhotoSerializer.Meta):
        fields = ('id', 'name', 'url')
