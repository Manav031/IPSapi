from django.contrib import admin
from .models import AccessPoint, Building, Location

# Register your models here.
admin.site.register(AccessPoint)
admin.site.register(Building)
admin.site.register(Location)