from django.contrib import admin

# Register your models here.

from .models import DailyPrice,SelectedPrice

admin.site.register(DailyPrice)
admin.site.register(SelectedPrice)


