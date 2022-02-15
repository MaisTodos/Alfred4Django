from decimal import Decimal
from django.db import models


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


