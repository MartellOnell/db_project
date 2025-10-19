from django.db import models
from django.contrib.auth import get_user_model

from apps.deals.models.menu import MenuItem


User = get_user_model()


class OrderMenuItem(models.Model):
    dish = models.ForeignKey(
        to=MenuItem,
        on_delete=models.CASCADE,
        verbose_name='dish',
    )

    quantity = models.PositiveIntegerField(
        verbose_name='quantity',
        default=1,
    )

    guest = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='order_menu_items',
        verbose_name='guest',
    )


    class Meta:
        verbose_name = 'order menu'
        verbose_name_plural = 'order menu'
