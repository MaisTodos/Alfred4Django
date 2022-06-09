from django.forms import ValidationError
from validate_docbr import CNPJ, CPF


def cnpj_validator(value: str):
    if not CNPJ().validate(value):
        raise ValidationError(message="CNPJ inválido.")


def cpf_validator(value: str):
    if not CPF().validate(value):
        raise ValidationError(message="CPF inválido.")
