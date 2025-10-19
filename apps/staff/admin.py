from django.contrib import admin
from apps.staff import models

admin.site.register(models.Gender)
admin.site.register(models.CustomUser)
admin.site.register(models.JobPosition)