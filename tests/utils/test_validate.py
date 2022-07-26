import pytest
from django.forms import ValidationError

from alfred.utils.validate import cnpj_validator, cpf_validator


def test_cpf_validator():
    document = "78048208016"
    validated_doc = cpf_validator(value=document)

    assert validated_doc is None


def test_cpf_validator_error():
    document = "78048208013"

    with pytest.raises(ValidationError):
        validated_doc = cpf_validator(value=document)
        assert validated_doc == "CPF inválido."


def test_cnpj_validator():
    document = "23195245000117"
    validated_doc = cnpj_validator(value=document)

    assert validated_doc is None


def test_cnpj_validator_error():
    document = "23195245000112"

    with pytest.raises(ValidationError):
        validated_doc = cnpj_validator(value=document)
        assert validated_doc == "CNPJ inválido."


def test_cpf_validator_start_with_0():
    document = "3545054918"
    validated_doc = cpf_validator(value=document)

    assert validated_doc is None
