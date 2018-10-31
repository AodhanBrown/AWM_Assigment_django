from django.contrib import admin
from .models import Maps
# Register your models here.


@admin.register(Maps)
class MapsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'location', 'created')