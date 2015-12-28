# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404


class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serialized_user = serializer.data   # lista de diccionarios
        return Response(serialized_user)


class UserDetailAPI(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
