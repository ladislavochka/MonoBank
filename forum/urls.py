from django.urls import path

from .views import (
    ForumMessageCreateView,
    ForumMessageDeleteView,
    ForumMessageUpdateView,
    ForumTopicCreateView,
    ForumTopicDetailView,
    ForumTopicListView,
)


app_name = 'forum'


urlpatterns = [
    path(
        '',
        ForumTopicListView.as_view(),
        name='topic_list'
    ),

    path(
        'topic/<int:pk>/',
        ForumTopicDetailView.as_view(),
        name='topic_detail'
    ),

    path(
        'topic/create/',
        ForumTopicCreateView.as_view(),
        name='topic_create'
    ),

    path(
        'topic/<int:topic_id>/message/create/',
        ForumMessageCreateView.as_view(),
        name='message_create'
    ),

    path(
        'message/<int:pk>/edit/',
        ForumMessageUpdateView.as_view(),
        name='message_edit'
    ),

    path(
        'message/<int:pk>/delete/',
        ForumMessageDeleteView.as_view(),
        name='message_delete'
    ),
]