import random
from datetime import datetime
import string

from django.contrib.auth import get_user_model

from apps.staff.models import Gender
from utils.generate import string_generator


User = get_user_model()


def generate_user() -> None:
    User.objects.create_user(
        username=string_generator(10),
        password=string_generator(10),
        email=string_generator(10) + '@example.com',
        phone='+7123456789',
        gender=Gender.objects.get(pk=random.randint(1, 2)),
        birthday=datetime.now().date(),
        passport_series=string_generator(4, chars=string.digits),
        passport_number=string_generator(6, chars=string.digits),
    )