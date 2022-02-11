from alfred.forms.forms_fields import BRPhoneNumberField
from phonenumber_field.formfields import PhoneNumberField
from unittest.mock import patch


def test_br_phone_number_field():
    assert issubclass(BRPhoneNumberField, PhoneNumberField)


def test_br_phone_number_format_number():
    function = BRPhoneNumberField()
    value = "(019) 99106 1478"
    expected_value = "+55019991061478"
    new_value = function._format_number(value)

    assert new_value == expected_value


@patch("alfred.forms.forms_fields.BRPhoneNumberField.to_python")
def test_br_phone_number_to_python(mock_function):
    value = "(019) 99106 1478"

    function = BRPhoneNumberField()
    function.to_python(value)

    mock_function.assert_called_once()
    mock_function.assert_called_once_with(value)


@patch("alfred.forms.forms_fields.BRPhoneNumberField.clean")
def test_br_phone_number_clean(mock_function):
    value = "+55019991061478"

    function = BRPhoneNumberField()
    function.clean(value)

    mock_function.assert_called_once()
    mock_function.assert_called_once_with(value)
