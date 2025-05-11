import random

from django.contrib.auth import get_user_model

from apps.deals.models import Room
from apps.deals.models import MenuItem

from utils.generate import string_generator


User = get_user_model()


def generate_room() -> None:
    user_ids = list(User.objects.values_list('id', flat=True))
    random_id = random.choice(user_ids)
    Room.objects.create(
        employee=User.objects.get(id=random_id),
    )


def generate_menu_item() -> None:
    MenuItem.objects.create(
        dish_name='dish_name ' + string_generator(5),
        calories=random.randint(10, 100),
    )