from alfred.models.fields import OnlyDigitsField
from alfred.utils.validate import cnpj_validator, cpf_validator


class CnpjField(OnlyDigitsField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(cnpj_validator)


class CpfField(OnlyDigitsField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(cpf_validator)
