from django.utils import timezone
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)

from .models import (
    News,
    Event,
    Announcement,
    Material,
)


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        now = timezone.now()

        context['news'] = News.objects.order_by(
            '-created_at'
        )[:3]

        context['events'] = Event.objects.filter(
            date__gte=now
        ).order_by(
            'date'
        )[:3]

        context['announcements'] = Announcement.objects.order_by(
            '-created_at'
        )[:3]

        context['materials'] = Material.objects.order_by(
            '-created_at'
        )[:3]

        return context


class NewsListView(ListView):
    model = News
    template_name = 'core/news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.order_by('-created_at')


class NewsDetailView(DetailView):
    model = News
    template_name = 'core/news_detail.html'
    context_object_name = 'news'


class EventListView(ListView):
    model = Event
    template_name = 'core/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.order_by('date')


class EventDetailView(DetailView):
    model = Event
    template_name = 'core/event_detail.html'
    context_object_name = 'event'


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'core/announcement_list.html'
    context_object_name = 'announcements'

    def get_queryset(self):
        return Announcement.objects.order_by('-created_at')


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'core/announcement_detail.html'
    context_object_name = 'announcement'


class MaterialListView(ListView):
    model = Material
    template_name = 'core/material_list.html'
    context_object_name = 'materials'

    def get_queryset(self):
        return Material.objects.order_by('-created_at')


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'core/material_detail.html'
    context_object_name = 'material'