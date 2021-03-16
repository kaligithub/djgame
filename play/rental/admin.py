from django.contrib import admin

from play.base.admin import ChangedDataSimpleHistoryAdmin, InputFilter
from play.rental.models import Friend, Belonging, Borrowed



@admin.register(Friend)
class FriendAdmin(ChangedDataSimpleHistoryAdmin):

    list_display = (
        'name',
    )
    
    search_fields = (
        'name',
    )

    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'name',
    )

@admin.register(Belonging)
class BelongingAdmin(ChangedDataSimpleHistoryAdmin):

    list_display = (
        'name',
    )
    
    search_fields = (
        'name',
    )

    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'name',
    )


@admin.register(Borrowed)
class BorrowedAdmin(ChangedDataSimpleHistoryAdmin):

    list_display = (
        'what',
        'to_who',
        'when',
        'returned',

    )
    
    search_fields = (
        'what',
        'to_who',
        'when',
        'returned',
    )

    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'what',
        'to_who',
        'when',
        'returned',
    )

    