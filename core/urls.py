from django.urls import path

from .views import (
    HomeView,
    NewsListView,
    NewsDetailView,
    AnnouncementListView,
    AnnouncementDetailView,
    MaterialListView,
    MaterialDetailView,
    GradeListView,
)


urlpatterns = [
    path(
        '',
        HomeView.as_view(),
        name='home'
    ),

    path(
        'news/',
        NewsListView.as_view(),
        name='news_list'
    ),

    path(
        'news/<int:pk>/',
        NewsDetailView.as_view(),
        name='news_detail'
    ),

    path(
        'announcements/',
        AnnouncementListView.as_view(),
        name='announcement_list'
    ),

    path(
        'announcements/<int:pk>/',
        AnnouncementDetailView.as_view(),
        name='announcement_detail'
    ),

    path(
        'materials/',
        MaterialListView.as_view(),
        name='material_list'
    ),

    path(
        'materials/<int:pk>/',
        MaterialDetailView.as_view(),
        name='material_detail'
    ),

    path(
        'grades/',
        GradeListView.as_view(),
        name='grade_list'
    ),
]