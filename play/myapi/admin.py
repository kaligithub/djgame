from django.contrib import admin

from play.base.admin import ChangedDataSimpleHistoryAdmin, InputFilter
from play.myapi.models import Hero


@admin.register(Hero)
class HeroAdmin(ChangedDataSimpleHistoryAdmin):
    
    list_display = (
        'name',
        'alias',
    )

    search_fields = (
        'name',
        'aliase',
    )

    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'name',
        'alias',
    )


