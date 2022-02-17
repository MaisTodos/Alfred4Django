from unittest.mock import patch

import pytest

from alfred.mixins.geolocation import AnnotateGeolocationMixin
from generic.models import GenericModel

pytestmark = pytest.mark.django_db


@patch("alfred.mixins.geolocation.AnnotateGeolocationMixin.distance")
def test_annotate_geolocation_mixin_with_mock(mock_function):
    lat, lon = 36.4766, -95.0192

    function = AnnotateGeolocationMixin()
    function.distance(lat, lon)

    mock_function.assert_called_once()
    mock_function.assert_called_once_with(lat, lon)


def test_annotate_geolocation_mixin():
    lat = "36.4766"
    lon = "-95.0192"

    model = GenericModel()
    model.latitude = lat
    model.longitude = lon
    model.save()

    queryset = GenericModel.geolocation
    queryset.distance(lat, lon)

    assert queryset.count() == 1


def test_annotate_geolocation_mixin_without_queryset():
    lat = "36.4766"
    lon = "-95.0192"

    queryset = GenericModel.geolocation
    queryset.distance(lat, lon)

    assert queryset.count() == 0
