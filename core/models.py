from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
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


class Grade(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='grades',
        verbose_name='Учень'
    )

    subject = models.CharField(
        max_length=100,
        verbose_name='Предмет'
    )

    grade = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12),
        ],
        verbose_name='Оцінка'
    )

    date_received = models.DateField(
        verbose_name='Дата отримання оцінки'
    )

    work_title = models.CharField(
        max_length=200,
        verbose_name='Назва роботи / тема'
    )

    teacher_comment = models.TextField(
        blank=True,
        verbose_name='Коментар викладача'
    )

    class Meta:
        ordering = ['-date_received', '-id']
        verbose_name = 'Оцінка'
        verbose_name_plural = 'Оцінки'

    def __str__(self):
        return f'{self.student.username} — {self.subject}: {self.grade}'