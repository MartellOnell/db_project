from django.db import models

from apps.staff.models.choices import GenderValueChoices


class Gender(models.Model):
    value = models.CharField(
        verbose_name='Значение',
        choices=GenderValueChoices.choices,
        max_length=1,
    )

    class Meta:
        verbose_name = "Gener"
        verbose_name_plural = "Genders"
