from alfred.drf import MultiSerializerMixin


def test_multiserializermixin():
    mixin = MultiSerializerMixin()
    mixin.action = "default"
    assert mixin.get_serializer_class() == mixin.serializers.get("default")
