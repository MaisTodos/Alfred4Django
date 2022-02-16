from django.db import models
from alfred.mixins.geolocation import AnnotateGeolocationMixin


class GeolocationManager(AnnotateGeolocationMixin, models.Manager):
    pass


class GenericModel(models.Model):
    latitude = models.CharField(
        blank=True, 
        null=True, 
        verbose_name="Latitude", 
        max_length=50, 
        db_index=True,
    )
    longitude = models.CharField(
        blank=True,
        null=True,
        verbose_name="Longitude",
        max_length=50,
        db_index=True,
    )
    geolocation = GeolocationManager()

