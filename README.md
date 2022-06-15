# Alfred para Django

![Alfred](https://upload.wikimedia.org/wikipedia/commons/8/80/Alfred_Thaddeus_Crane_Pennyworth.jpg)

Alfred Thaddeus Crane Pennyworth é um personagem fictício da DC Comics. Ele é mordomo e tutor do bilionário Bruce Wayne.

Alfred tem sua origem muitas vezes envolta em mistério e pouco se fala de suas atividades antes de ele se tornar mordomo da rica e tradicional família Wayne. Em algumas mini-series e edições avulsas das HQs fala-se de sua distante ligação com a Scotland Yard onde ele teria trabalhado como um de seus agentes mais discretos.

Sabe-se ainda de um passado como ator competente, tendo essa experiência na dramaturgia se provado útil em diversas ocasiões. Como, por exemplo, tendo ensinado ao Bruce, ainda jovem, como modificar sua voz para imitar as vozes de outras pessoas. Algo que se provou muito útil na criação da persona do Homem-Morcego.

Demonstra também muitas outras habilidades úteis, como conhecimentos médicos básicos, por exemplo. Contudo, fica-se com a impressão que nem Bruce Wayne conhece totalmente esse passado de seu mordomo. Muitas vezes, as palavras de Alfred são sugestões quase que subliminares que ajudam o "cruzado mascarado" na solução de enigmas complexos de crimes. Mesmo assim, Alfred, várias vezes, faz o papel de ingênuo.

## Rodando o projeto local

Primeiramente você deve instanciar o docker com o comando

```bash
make build
```

Após o build, é só rodar os testes

```bash
make test
```

## DRF

Esta lib possui alguns helpers para o DRF

### helpers

#### MultiSerializerMixin

Quando precisar alterar um serializer de um viewset do DRF, é só utilizar o MultiSerializerMixin, e setar na própria classe o dict com o serializer

```python
from alfred.drf import MultiSerializerMixin
from rest_framework import mixins, viewsets

class FooBillViewSet(
    MultiSerializerMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Foo.objects.all()
    serializers = {
        "default": FooSerializer,
        "list": FooListSerializer,
        "create": FooCreateSerializer,
        "retrieve": FooSerializer,
    }
    filterset_class = FooBillFilter
    schema = AutoSchema(tags=["foo"])
```

### Classes Mixin para uso no admin

#### NotAddMixin

Não possui permissão para adcionar informações no banco de dados.

```python
class NotAddMixin(object):
    def has_add_permission(self, request, obj=None):
        return False
```

#### NotDeleteMixin

Não possui permissão para deletar informações no banco de dados.

```python
class NotDeleteMixin(object):
    def has_delete_permission(self, request, obj=None):
        return False
```

#### NotChangeMixin

Não possui permissão para alterar informações no banco de dados

```python
class NotChangeMixin(object):
    def has_change_permission(self, request, obj=None):
        return False
```

#### ChangeOnlyAdminMixin

Tem como heranças as classes NotDeleteMixin, NotAddMixin e suas respectivas funções.

```python
class ChangeOnlyAdminMixin(NotDeleteMixin, NotAddMixin):
    pass
```

#### ReadOnlyAdminMixin

Tem como heranças as classes ChangeOnlyAdminMixin, NotChangeMixin e suas respectivas funções.

```python
class ReadOnlyAdminMixin(ChangeOnlyAdminMixin, NotChangeMixin):
    extra = 0
    max_num = 0
    can_delete = False
```

#### CreateOnlyAdminMixin

Tem como heranças as classes NotDeleteMixin, NotChangeMixin e suas respectivas funções.

```python
class CreateOnlyAdminMixin(NotDeleteMixin, NotChangeMixin):
    extra = 0
    max_num = 0
    can_delete = False
```

#### FieldsReadOnlyAdminMixin

Retorna os campos somente leitura.

```python
class FieldsReadOnlyAdminMixin(object):
    excluded_readonly = []

    def get_readonly_fields(self, request, obj=None):
        return [
            f.name
            for f in self.model._meta.fields
            if f.name not in self.excluded_readonly
        ]
```

### Forms

#### BRPhoneNumberField

O field `BRPhoneNumberField` utiliza mascara "(00) 00000-0000" para salvar os dados no banco de dados. Para utilizar esse campo é necessário o pacote `phonenumbers`.

```python
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
```

### Mixins

#### AnnotateGeolocationMixin

Essa classe `Mixin` tem como objetivo retornar a distância esférica entre dois pontos.

- Defina um model com herança da classe `AnnotateGeolocationMixin`.

```python
class Store(AnnotateGeolocationMixin, models.Model):
    ...
```

- Defina a classe `ViewSet` com queryset referenciando o `model` com AnnotateGeolocationMixin.

```python
class StoreListViewSet(ListAPIView):
    queryset = Store.objects.all
    lat, lon, radius = 36.4766, -95.0192, 50

    return queryset.distance(lat, lon).filter(distance_km__lte=radius)
```

### Models

#### ChoiceField

- O field `ChoiceField` é uma classe para ser usada na definição de choices dentro de um model Django. Exemplo de utilização:

```python
from model_utils.fields import StatusField
from model_utils.choices import Choices

class Order(AbstractBaseModel):
    STATUS_CHOICES = Choices(
        ("created", "Criado"),
        ("received", "Recebido"),
        ("confirmed", "Confirmado"),
        ("canceled", "Cancelado"),
    )
    status = ChoiceField(
        verbose_name=_("Status"),
        default="created",
        max_length=40,
        choices_name="STATUS_CHOICES",
    )
```

- STATUS_CHOICES deve estar definindo dentro da classe. 
- o campo `choices_name` deve ser definido igual ao Choices em formato string.

#### OnlyDigitsField

Campo `OnlyDigitsField` tem como objetivo armazenar dados de telefone.

```python
class Store(models.Model):
    phone = OnlyDigitsField(
        blank=True,
        null=True,
        verbose_name=_("Telefone de contato principal"),
        max_length=30,
    )
```

#### CpfField e CnpjField

Os campos CpfField e CnpjField fazem a validação dos números dos documentos brasileiros. Herdam a classe OnlyDigitsField e dependem da lib validate_docbr.

```python
class CpfField(OnlyDigitsField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(cpf_validator)

class CnpjField(OnlyDigitsField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(cnpj_validator)
```