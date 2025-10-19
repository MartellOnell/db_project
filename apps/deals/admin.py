from django.contrib import admin

from apps.deals import models

admin.site.register(models.Room)
admin.site.register(models.Booking)
admin.site.register(models.MenuItem)
admin.site.register(models.OrderMenuItem)