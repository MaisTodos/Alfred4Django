class NotAddMixin(object):
    def has_add_permission(self, request, obj=None):
        return False


class NotDeleteMixin(object):
    def has_delete_permission(self, request, obj=None):
        return False


class NotChangeMixin(object):
    def has_change_permission(self, request, obj=None):
        return False


class ChangeOnlyAdminMixin(NotDeleteMixin, NotAddMixin):
    pass


class ReadOnlyAdminMixin(ChangeOnlyAdminMixin, NotChangeMixin):
    extra = 0
    max_num = 0
    can_delete = False


class CreateOnlyAdminMixin(NotDeleteMixin, NotChangeMixin):
    extra = 0
    max_num = 0
    can_delete = False


class FieldsReadOnlyAdminMixin(object):
    excluded_readonly = []

    def get_readonly_fields(self, request, obj=None):
        return [
            f.name
            for f in self.model._meta.fields
            if f.name not in self.excluded_readonly
        ]
