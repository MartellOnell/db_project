from django.db import models


class JobPosition(models.Model):
    title = models.CharField(
        verbose_name="title",
        max_length=100,
    )

    salary = models.DecimalField(
        verbose_name="salary",
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    class Meta:
        verbose_name = "job position"
        verbose_name_plural = "job positions"