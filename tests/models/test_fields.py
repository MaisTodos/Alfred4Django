from django.db import models

from alfred.models.fields import OnlyDigitsField, only_digits


def test_only_digits_issubclass():
    assert issubclass(OnlyDigitsField, models.CharField)


def test_only_digits():
    value = "60.119.993/0001-47"
    only_digits_value = only_digits(value)
    expected_value = "60119993000147"

    assert only_digits_value == expected_value


def test_to_python():
    obj = OnlyDigitsField()
    value = "60.119.993/0001-47"
    expected_value = "60119993000147"

    only_digits_value = obj.to_python(value)

    assert only_digits_value == expected_value


def test_formfield_with_form_max_length():
    obj = OnlyDigitsField(max_length=14, form_max_length=18)
    form_field = obj.formfield()

    assert form_field.max_length == 18
