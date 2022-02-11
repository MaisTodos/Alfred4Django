import re

from phonenumber_field.formfields import PhoneNumberField


class BRPhoneNumberField(PhoneNumberField):
    def __init__(self, *args, region=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget.input_type = "text"
        self.error_messages["invalid"] = "Número de celular inválido!"

    def _format_number(self, value):
        value = "".join(re.findall(r"\d+", value or ""))
        return f"+55{value}"

    def to_python(self, value):
        value = self._format_number(value)  # pragma: no cover
        phone_number = super().to_python(value)  # pragma: no cover
        return str(phone_number)  # pragma: no cover

    def clean(self, value):
        value = super().clean(value)  # pragma: no cover
        return value.replace("+55", "")  # pragma: no cover
