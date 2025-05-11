from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Room(models.Model):
    condition = models.CharField(
        verbose_name='condition',
        max_length=50,
        default='Clean',
    )

    status = models.CharField(
        verbose_name='status',
        max_length=50,
        default='Available',
    )

    employee = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        verbose_name='employee',
        null=True,
    )

    class Meta:
        verbose_name = 'room'
        verbose_name_plural = 'rooms'
