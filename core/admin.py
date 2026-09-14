from django.contrib import admin

from .models import (
    News,
    Event,
    Announcement,
    Material,
    Grade,
)


admin.site.register(News)
admin.site.register(Event)
admin.site.register(Announcement)
admin.site.register(Material)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'subject',
        'grade',
        'date_received',
        'work_title',
    )

    search_fields = (
        'student__username',
        'student__first_name',
        'student__last_name',
        'subject',
        'work_title',
    )

    list_filter = (
        'student',
        'subject',
        'date_received',
        'grade',
    )

    ordering = (
        '-date_received',
        '-id',
    )