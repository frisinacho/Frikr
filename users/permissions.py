# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, POST, PUT o DELETE)
        """
        # Si quiere crear un usuario, sea quien sea puede
        if view.action == 'create':
            return True
        # Si no es POST, el superusuario siempre puede
        elif request.user.is_superuser:
            return True
        # Si es un GET a la vista  de detalle, tomo la decisión  en has_object_permission
        elif view.action in ['retrieve', 'update', 'destroy']:
            return True
        else:
            # GET a /api/1.0/photos/
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, PUT o DELETE)
        sobre el objeto 'obj'
        """
        # Si es superusuario, o el usuario autenticado intenta
        # hacer GET, PUT o DELETE sobre su mismo perfil
        return request.user.is_superuser or request.user == obj
