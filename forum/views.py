from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count, Value
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ForumMessageForm, ForumTopicForm
from .models import ForumMessage, ForumTopic


class ForumTopicListView(ListView):
    model = ForumTopic
    template_name = 'forum/topic_list.html'
    context_object_name = 'topics'

    def get_queryset(self):
        return (
            ForumTopic.objects
            .select_related('author')
            .annotate(message_count=Count('messages') + Value(1))
        )


class ForumTopicDetailView(DetailView):
    model = ForumTopic
    template_name = 'forum/topic_detail.html'
    context_object_name = 'topic'

    def get_queryset(self):
        return (
            ForumTopic.objects
            .select_related('author')
            .prefetch_related('messages__author')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        context['can_moderate'] = (
            user.is_authenticated
            and (
                user.is_staff
                or user.is_superuser
                or user.groups.filter(name__iexact='Moderator').exists()
            )
        )

        return context


class ForumTopicCreateView(LoginRequiredMixin, CreateView):
    model = ForumTopic
    form_class = ForumTopicForm
    template_name = 'forum/topic_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class ForumMessageCreateView(LoginRequiredMixin, CreateView):
    model = ForumMessage
    form_class = ForumMessageForm
    template_name = 'forum/message_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.topic = get_object_or_404(
            ForumTopic,
            pk=kwargs['topic_id']
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic = self.topic

        self.object = form.save()

        return redirect(
            'forum:topic_detail',
            pk=self.topic.pk
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = self.topic
        return context


class ForumMessageUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    model = ForumMessage
    form_class = ForumMessageForm
    template_name = 'forum/message_form.html'
    context_object_name = 'message'

    def test_func(self):
        message = self.get_object()

        return (
            message.author == self.request.user
            or self.request.user.is_staff
            or self.request.user.is_superuser
            or self.request.user.groups.filter(
                name__iexact='Moderator'
            ).exists()
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = self.object.topic
        return context

    def get_success_url(self):
        return self.object.topic.get_absolute_url()


class ForumMessageDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = ForumMessage
    template_name = 'forum/message_confirm_delete.html'

    def test_func(self):
        message = self.get_object()

        return (
            message.author == self.request.user
            or self.request.user.is_staff
            or self.request.user.is_superuser
            or self.request.user.groups.filter(
                name__iexact='Moderator'
            ).exists()
        )

    def get_success_url(self):
        return self.object.topic.get_absolute_url()