# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, POST, PUT o DELETE)
        """
        pass

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, POST, PUT o DELETE)
        sobre el objeto 'obj'
        """
        pass
