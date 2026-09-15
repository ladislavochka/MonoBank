import calendar
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import EventForm
from .models import Event


class EventPermissionMixin(
    LoginRequiredMixin,
    UserPassesTestMixin
):
    def test_func(self):
        user = self.request.user

        return (
            user.is_staff
            or user.is_superuser
            or user.groups.filter(
                name__iexact='Moderator'
            ).exists()
        )

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('event_list')

        return super().handle_no_permission()


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.select_related(
            'organizer'
        ).order_by('start_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        now = timezone.now()
        today = timezone.localdate()

        events = list(context['events'])

        context['future_events'] = [
            event
            for event in events
            if event.start_at > now
            and event.start_at.date() != today
        ]

        context['today_events'] = [
            event
            for event in events
            if event.start_at.date() == today
        ]

        context['past_events'] = [
            event
            for event in events
            if event.start_at < now
            and event.start_at.date() != today
        ]

        context['can_manage_events'] = (
            self.request.user.is_authenticated
            and (
                self.request.user.is_staff
                or self.request.user.is_superuser
                or self.request.user.groups.filter(
                    name__iexact='Moderator'
                ).exists()
            )
        )

        # Поточний місяць для календаря
        current_date = today

        context['calendar_year'] = current_date.year
        context['calendar_month'] = current_date.month
        context['calendar_month_name'] = calendar.month_name[
            current_date.month
        ]

        calendar_data = calendar.monthcalendar(
            current_date.year,
            current_date.month
        )

        events_by_day = {}

        for event in events:
            event_date = event.start_at.date()

            if (
                event_date.year == current_date.year
                and event_date.month == current_date.month
            ):
                events_by_day.setdefault(
                    event_date.day,
                    []
                ).append(event)

        context['calendar_data'] = calendar_data
        context['events_by_day'] = events_by_day

        return context


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_queryset(self):
        return Event.objects.select_related(
            'organizer'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        context['can_manage_events'] = (
            user.is_authenticated
            and (
                user.is_staff
                or user.is_superuser
                or user.groups.filter(
                    name__iexact='Moderator'
                ).exists()
            )
        )

        return context


class EventCreateView(EventPermissionMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class EventUpdateView(EventPermissionMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class EventDeleteView(EventPermissionMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'

    def get_success_url(self):
        return '/events/'
