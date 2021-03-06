# Generated by Django 2.2.27 on 2022-02-15 20:53

from django.db import migrations, models

import alfred.mixins.geolocation


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GenericModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "latitude",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=50,
                        null=True,
                        verbose_name="Latitude",
                    ),
                ),
                (
                    "longitude",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=50,
                        null=True,
                        verbose_name="Longitude",
                    ),
                ),
            ],
            bases=(alfred.mixins.geolocation.AnnotateGeolocationMixin, models.Model),
        ),
    ]
