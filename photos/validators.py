# -*- coding: utf-8 -*-


def badwords_detector(value):
        """
        Valida si en 'value' se han puesto tacos definidos en settings.BADWORDS
        :return: Boolean
        """
        cleaned_data = super(PhotoForm, self).clean()

        description = cleaned_data.get('description', '')

        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise ValidationError(u'La palabra {0} no está permitida'.format(badword))

        # Si todo va OK, devuelvo los datos limpios/normalizados
        return cleaned_data
