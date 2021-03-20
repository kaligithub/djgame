from django.contrib import admin

from play.base.admin import ChangedDataSimpleHistoryAdmin, InputFilter
from play.employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(ChangedDataSimpleHistoryAdmin):

    readonly_fields = (
        'id',
    )

    list_display = (
        'name',
        'email',
    )

    search_fields = (
        'name',
        'email',
    )

    list_filter = (
        'name',
        'email',
    )


