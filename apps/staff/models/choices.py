from django.db.models import TextChoices


class GenderValueChoices(TextChoices):
    M = "M", "Male"
    F = "F", "Female"
