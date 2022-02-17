from django.db import models


def only_digits(value: str):
    return "".join(filter(lambda i: i.isdigit(), value))


class OnlyDigitsField(models.CharField):
    def __init__(self, *args, form_max_length=None, **kwargs):
        self.form_max_length = form_max_length
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        if self.form_max_length:
            kwargs["max_length"] = self.form_max_length
        return super().formfield(**kwargs)

    def to_python(self, value):
        return value and only_digits(value)
