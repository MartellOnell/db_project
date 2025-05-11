from django.db import models
from django.utils import timezone


class MenuItem(models.Model):
    serve_date = models.DateField(
        verbose_name='serving date',
        null=True,
        blank=True,
        default=timezone.now,
    )

    dish_name = models.CharField(
        verbose_name='dish name',
    )

    calories = models.PositiveIntegerField(
        verbose_name='calories',
    )

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'
