import logging

from django import forms

from alfred.forms.forms_fields import BRPhoneNumberField

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    phone = BRPhoneNumberField(
        label="Telefone Celular*",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                "data-mask": "(00) 00000-0000",
                "class": "form-control",
                "placeholder": "(00) 00000-0000",
            }
        ),
    )
