from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from play.base.models import APIKey


class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the 'all' option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v) for k, v in changelist.get_filters_params().items() if k != self.parameter_name
        )
        yield all_choice


class ChangedDataSimpleHistoryAdmin(SimpleHistoryAdmin):
    """
    Custom history settings for displaying changed fields and changed values
    """

    history_list_display = ['changed_fields', 'changed_values', 'ip_address']

    def changed_fields(self, obj):
        """
        Function for getting the changed fields
        """
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            return delta.changed_fields
        return None

    def changed_values(self, obj):
        """
        Function for getting the changed values with respective fields
        """
        changed_fields = self.changed_fields(obj) or []
        changed_values = {}
        for fields in changed_fields:
            changed_values.update(
                {fields: [obj.__getattribute__(fields), obj.prev_record.__getattribute__(fields)]}
            )
        return changed_values


@admin.register(APIKey)
class APIKeyAdmin(ChangedDataSimpleHistoryAdmin):
    list_display = (
        'id',
        'api_key',
        'api_secret_key',
        'is_active',
    )

    readonly_fields = (
        'id',
        'api_key',
        'api_secret_key',
    )
