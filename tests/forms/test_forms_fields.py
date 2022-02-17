from unittest.mock import patch

from phonenumber_field.formfields import PhoneNumberField

from generic.forms import BRPhoneNumberField


def test_br_phone_number_field():
    assert issubclass(BRPhoneNumberField, PhoneNumberField)


def test_br_phone_number_format_number():
    value = "(019) 99106 1478"
    expected_value = "+55019991061478"

    function = BRPhoneNumberField()
    new_value = function._format_number(value)

    assert new_value == expected_value


def test_br_phone_number_to_python():
    value = "(019) 99106 1478"
    expected_value = "+5519991061478"

    function = BRPhoneNumberField()
    new_value = function.to_python(value)

    assert new_value == expected_value


def test_br_phone_number_clean():
    value = "(019) 99106 1478"
    expected_value = "19991061478"

    function = BRPhoneNumberField()
    new_value = function.clean(value)

    assert new_value == expected_value


@patch("alfred.forms.forms_fields.BRPhoneNumberField.to_python")
def test_br_phone_number_to_python_mock(mock_function):
    value = "(019) 99106 1478"

    function = BRPhoneNumberField()
    function.to_python(value)

    mock_function.assert_called_once()
    mock_function.assert_called_once_with(value)


@patch("alfred.forms.forms_fields.BRPhoneNumberField.clean")
def test_br_phone_number_clean_mock(mock_function):
    value = "+55019991061478"

    function = BRPhoneNumberField()
    function.clean(value)

    mock_function.assert_called_once()
    mock_function.assert_called_once_with(value)
