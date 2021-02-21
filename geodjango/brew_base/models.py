from django.contrib.gis.db import models

class BrewPoint(models.Model):
    # Django fields that correspond to attributes in brew_eng gpkg
    name = models.CharField('Name', max_length=100, null=True)
    street = models.CharField('Street', max_length=100, null=True)
    postcode = models.CharField('Postcode', max_length=20, null=True)
    city = models.CharField('City', max_length=50, null=True)
    website = models.CharField('Website', max_length=200, null=True)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    point = models.PointField()

    def __str__(self):
        return self.name
