from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(
        max_length=200,
        blank=True
    )

    class Meta:
        ordering = ['date']
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Матеріал'
        verbose_name_plural = 'Матеріали'

    def __str__(self):
        return self.title