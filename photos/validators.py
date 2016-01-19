# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from photos.settings import BADWORDS


def badwords_detector(value):
        """
        Valida si en 'value' se han puesto tacos definidos en settings.BADWORDS
        :return: Boolean
        """

        for badword in BADWORDS:
            if badword.lower() in value.lower():
                raise ValidationError(u'La palabra {0} no está permitida'.format(badword))

        # Si todo va OK, devuelvo los datos limpios/normalizados
        return True
