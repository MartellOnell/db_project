from django.db import models
from django.contrib.auth import get_user_model

from apps.deals.models.room import Room
from apps.deals.models.order_menu import OrderMenuItem


User = get_user_model()


class Booking(models.Model):
    room = models.ForeignKey(
        to=Room,
        on_delete=models.CASCADE,
    )

    guest = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name='guest',
    )

    checkin = models.DateField(
        verbose_name='checkin date',
    )

    order_menu = models.ForeignKey(
        to=OrderMenuItem,
        on_delete=models.CASCADE,
        verbose_name='order menu',
        related_name='bookings_order_menu_items',
        null=True,
    )

    checkout = models.DateField(
        verbose_name='checkout date',
    )

    class Meta:
        verbose_name = 'booking'
        verbose_name_plural = 'bookings'
