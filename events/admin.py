from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'start_at',
        'end_at',
        'location',
        'organizer',
    )

    search_fields = (
        'title',
        'description',
        'location',
        'organizer__username',
    )

    list_filter = (
        'start_at',
        'created_at',
    )

    date_hierarchy = 'start_at'

    ordering = (
        'start_at',
    )
