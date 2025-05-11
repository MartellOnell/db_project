from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from apps.staff.models.gender import Gender
from apps.staff.models.job_position import JobPosition


class CustomUser(AbstractUser):
    is_owner = models.BooleanField(
        verbose_name='the owner of the establishment',
        default=False,
    )

    phone = models.CharField(
        verbose_name='phone number',
        validators=[
            RegexValidator(
                regex=r'^\+?7?\d[9,15]$',
                message="Phone number must be entered in the format '+7123456789'. Up to 15 digits allowed."
            ),
        ],
        max_length=17,
    )

    gender = models.ForeignKey(
        to=Gender,
        on_delete=models.PROTECT,
        verbose_name='gender',
    )

    position = models.ForeignKey(
        to=JobPosition,
        on_delete=models.PROTECT,
        verbose_name='job position',
        null=True,
    )

    birthday = models.DateField(
        verbose_name='birthday',
        null=True,
    )

    work_schedule = models.CharField(
        verbose_name='work schedule',
        max_length=100,
        null=True,
    )

    passport_series = models.CharField(
        verbose_name='passport series',
        max_length=4,
        null=True,
    )

    passport_number = models.CharField(
        verbose_name='passport number',
        max_length=6,
        null=True,
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
