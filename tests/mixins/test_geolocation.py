from unittest.mock import patch
from alfred.mixins.geolocation import AnnotateGeolocationMixin


@patch("alfred.mixins.geolocation.AnnotateGeolocationMixin.distance")
def test_annotate_geolocation_mixin(mock_function):
    lat, lon = 36.4766, -95.0192

    function = AnnotateGeolocationMixin()
    function.distance(lat, lon)

    mock_function.assert_called_once()
    mock_function.assert_called_once_with(lat, lon)
