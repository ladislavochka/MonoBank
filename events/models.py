from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Назва події'
    )

    description = models.TextField(
        verbose_name='Опис'
    )

    start_at = models.DateTimeField(
        verbose_name='Дата та час початку'
    )

    end_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата та час завершення'
    )

    location = models.CharField(
        max_length=255,
        verbose_name='Місце проведення'
    )

    organizer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='organized_events',
        verbose_name='Організатор'
    )

    online_url = models.URLField(
        blank=True,
        verbose_name='Посилання на онлайн-подію'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата оновлення'
    )

    class Meta:
        ordering = ['start_at']
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'event_detail',
            kwargs={'pk': self.pk}
        )

    @property
    def is_past(self):
        from django.utils import timezone

        return self.start_at < timezone.now()

    @property
    def is_today(self):
        from django.utils import timezone

        return self.start_at.date() == timezone.localdate()

    @property
    def is_future(self):
        from django.utils import timezone

        return self.start_at > timezone.now()

