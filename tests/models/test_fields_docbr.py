from alfred.models.fields import OnlyDigitsField
from alfred.models.fields_docbr import CnpjField, CpfField


def test_cnpj_field_issubclass():
    assert issubclass(CnpjField, OnlyDigitsField)


def test_cpf_field_issubclass():
    assert issubclass(CpfField, OnlyDigitsField)


def test_cnpj_class():
    cnpj = CnpjField()
    assert cnpj.serialize is True


def test_cpf_class():
    cpf = CpfField()
    assert cpf.serialize is True
