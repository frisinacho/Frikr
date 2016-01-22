# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from users.permissions import UserPermission
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


class UserViewSet(GenericViewSet):

    pagination_class = PageNumberPagination
    permission_classes = (UserPermission,)

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serialized_user = serializer.data   # lista de diccionarios
        return Response(serialized_user)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)    # Compruebo si el usuario auth puede hacer GET en este user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)    # Compruebo si el usuario auth puede hacer PUT en este user
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)    # Compruebo si el usuario auth puede hacer DELETE en este user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
