from django.contrib import admin

from play.base.admin import ChangedDataSimpleHistoryAdmin, InputFilter
from play.myapi.models import Hero


@admin.register(Hero)
class HeroAdmin(ChangedDataSimpleHistoryAdmin):
    
    list_display = (
        'name',
        'alias',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'name',
        'aliase',
    )

    readonly_fields = (
        'id',
    )

    list_filter = (
        'name',
        'alias',
    )


