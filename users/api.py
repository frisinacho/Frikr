# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.views.generic import View
from users.serializers import UserSerializer


class UserListAPI(View):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
