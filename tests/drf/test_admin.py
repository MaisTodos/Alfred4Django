from alfred.drf.admin import (
    NotAddMixin,
    NotDeleteMixin,
    NotChangeMixin,
    ChangeOnlyAdminMixin,
    ReadOnlyAdminMixin,
    CreateOnlyAdminMixin,
    FieldsReadOnlyAdminMixin,
)


def test_not_add_mixin():
    mixin = NotAddMixin()
    assert mixin.has_add_permission("foo") is False


def test_not_delete_mixin():
    mixin = NotDeleteMixin()
    assert mixin.has_delete_permission("foo") is False


def test_not_change_mixin():
    mixin = NotChangeMixin()
    assert mixin.has_change_permission("foo") is False


def test_change_only_admin_mixin():
    mixin = ChangeOnlyAdminMixin()
    assert mixin.has_add_permission("foo") is False
    assert mixin.has_delete_permission("foo") is False


def test_read_only_admin_mixin():
    mixin = ReadOnlyAdminMixin()
    assert mixin.has_add_permission("foo") is False
    assert mixin.has_delete_permission("foo") is False
    assert mixin.has_change_permission("foo") is False
    assert mixin.extra == 0
    assert mixin.max_num == 0
    assert mixin.can_delete is False


def test_create_only_admin_mixin():
    mixin = CreateOnlyAdminMixin()
    assert mixin.has_delete_permission("foo") is False
    assert mixin.has_change_permission("foo") is False
    assert mixin.extra == 0
    assert mixin.max_num == 0
    assert mixin.can_delete is False


# def test_fields_readonly_admin_mixin_empty_excluded():
#     mixin = FieldsReadOnlyAdminMixin()
#     mixin.model = AbstractBaseModel()

#     assert mixin.excluded_readonly == []
#     readonly_fields = mixin.get_readonly_fields(Mock(), Mock())
#     assert readonly_fields == ["created_at", "updated_at"]


# def test_fields_readonly_admin_mixin_with_excluded():
#     mixin = FieldsReadOnlyAdminMixin()
#     mixin.model = AbstractBaseModel()
#     mixin.excluded_readonly = ["created_at"]

#     readonly_fields = mixin.get_readonly_fields(Mock(), Mock())
#     assert readonly_fields == ["updated_at"]