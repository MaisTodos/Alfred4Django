# from unittest.mock import patch

from alfred.models.fields import OnlyDigitsField
from alfred.models.fields_docbr import CnpjField, CpfField


def test_cnpj_field_issubclass():
    assert issubclass(CnpjField, OnlyDigitsField)


def test_cpf_field_issubclass():
    assert issubclass(CpfField, OnlyDigitsField)


# @patch("alfred.models.fields.OnlyDigitsField.__init__")
# def test_cnpj_class(mock_class):
#     obj = CnpjField()
#     mock_class.assert_called_once()
