from django.contrib import admin

from play.base.admin import ChangedDataSimpleHistoryAdmin, InputFilter
from play.myapi.models import Hero, Place, Restaurant, Waiter



admin.site.register(Place)
admin.site.register(Restaurant)
#admin.site.register(Question)


@admin.register(Waiter)
class WaiterAdmin(ChangedDataSimpleHistoryAdmin):
    
    list_display = (
        'name',
        'restaurant',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'name',
        'restaurant',
    )

    readonly_fields = (
        'id',
    )

    list_filter = (
        'name',
        'restaurant',
    )


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




