from django.db import models


class Doctor(models.Model):
    """модель врача для хранения в базе данных"""
    
    name = models.CharField(max_length=200, verbose_name='ФИО')
    specialty = models.CharField(max_length=100, verbose_name='Специальность')
    clinic = models.CharField(max_length=200, verbose_name='Клиника')
    rating = models.IntegerField(default=5, verbose_name='Рейтинг')
    review = models.TextField(verbose_name='Отзыв')
    reviewer = models.CharField(max_length=100, verbose_name='Автор отзыва')

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return f"{self.name} ({self.specialty})"
