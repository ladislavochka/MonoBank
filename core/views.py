from django.utils import timezone
from django.views.generic import TemplateView

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

        context['announcements'] = (
            Announcement.objects.order_by(
                '-created_at'
            )[:3]
        )

        context['materials'] = Material.objects.order_by(
            '-created_at'
        )[:3]

        return context