from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)

from .models import (
    News,
    Announcement,
    Material,
    Grade,
)

from events.models import Event


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        now = timezone.now()

        context['news'] = News.objects.order_by(
            '-created_at'
        )[:3]

        context['events'] = Event.objects.filter(
            start_at__gte=now
        ).order_by(
            'start_at'
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
        return News.objects.order_by(
            '-created_at'
        )


class NewsDetailView(DetailView):
    model = News
    template_name = 'core/news_detail.html'
    context_object_name = 'news'


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'core/announcement_list.html'
    context_object_name = 'announcements'

    def get_queryset(self):
        return Announcement.objects.order_by(
            '-created_at'
        )


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'core/announcement_detail.html'
    context_object_name = 'announcement'


class MaterialListView(ListView):
    model = Material
    template_name = 'core/material_list.html'
    context_object_name = 'materials'

    def get_queryset(self):
        return Material.objects.order_by(
            '-created_at'
        )


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'core/material_detail.html'
    context_object_name = 'material'


class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = 'core/grade_list.html'
    context_object_name = 'grades'

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Grade.objects.select_related(
                'student'
            )
        else:
            queryset = Grade.objects.filter(
                student=self.request.user
            )

        subject = self.request.GET.get(
            'subject',
            ''
        ).strip()

        if subject:
            queryset = queryset.filter(
                subject__icontains=subject
            )

        if self.request.user.is_staff:
            student = self.request.GET.get(
                'student',
                ''
            ).strip()

            if student:
                queryset = queryset.filter(
                    student__username__icontains=student
                )

        sort = self.request.GET.get(
            'sort',
            '-date_received'
        )

        allowed_sorting = {
            'date': 'date_received',
            '-date': '-date_received',
            'subject': 'subject',
            '-subject': '-subject',
            'grade': 'grade',
            '-grade': '-grade',
        }

        order_by = allowed_sorting.get(
            sort,
            '-date_received'
        )

        return queryset.order_by(
            order_by,
            '-id'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['selected_subject'] = (
            self.request.GET.get(
                'subject',
                ''
            )
        )

        context['selected_student'] = (
            self.request.GET.get(
                'student',
                ''
            )
        )

        context['selected_sort'] = (
            self.request.GET.get(
                'sort',
                '-date_received'
            )
        )

        return context