from django.contrib.gis import admin
from .models import BrewPoint

admin.site.register(BrewPoint, admin.OSMGeoAdmin)
