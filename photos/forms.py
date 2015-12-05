# -*- coding: utf-8 -*-
from django import forms
from photos.models import Photo


class PhotoForm(forms.ModelForm):
    """
    Formulario para el modelo Photo
    """
    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):
        """
        Valida si en la descripción se han puesto tacos definidos en settings.BADWORDS
        :return: diccionario con los atributos si OK
        """
