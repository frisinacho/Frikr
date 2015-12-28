# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer


class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serialized_user = serializer.data   # lista de diccionarios
        return Response(serialized_user)
