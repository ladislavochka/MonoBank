from django.contrib import admin

from .models import (
    News,
    Event,
    Announcement,
    Material,
)


admin.site.register(News)
admin.site.register(Event)
admin.site.register(Announcement)
admin.site.register(Material)