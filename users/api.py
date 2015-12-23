# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from users.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer


class UserListAPI(View):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serialized_user = serializer.data   # lista de diccionarios
        renderer = JSONRenderer()
        json_users = renderer.render(serialized_user)   # lista de diccionarios -> JSON
        return HttpResponse(json_users)
