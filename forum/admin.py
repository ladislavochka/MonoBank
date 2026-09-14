from django.contrib import admin

from .models import ForumMessage, ForumTopic


@admin.register(ForumTopic)
class ForumTopicAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created_at',
    )
    search_fields = (
        'title',
        'text',
        'author__username',
    )
    list_filter = ('created_at',)


@admin.register(ForumMessage)
class ForumMessageAdmin(admin.ModelAdmin):
    list_display = (
        'topic',
        'author',
        'created_at',
    )
    search_fields = (
        'text',
        'author__username',
        'topic__title',
    )
    list_filter = ('created_at',)