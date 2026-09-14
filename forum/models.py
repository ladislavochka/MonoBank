from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


class ForumTopic(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        verbose_name='Назва теми'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='forum_topics',
        verbose_name='Автор'
    )
    text = models.TextField(
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(5000)
        ],
        verbose_name='Перше повідомлення'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Тема форуму'
        verbose_name_plural = 'Теми форуму'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'forum:topic_detail',
            kwargs={'pk': self.pk}
        )


class ForumMessage(models.Model):
    topic = models.ForeignKey(
        ForumTopic,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Тема'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='forum_messages',
        verbose_name='Автор'
    )
    text = models.TextField(
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(5000)
        ],
        verbose_name='Повідомлення'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Повідомлення форуму'
        verbose_name_plural = 'Повідомлення форуму'

    def __str__(self):
        return f'{self.author.username}: {self.text[:50]}'