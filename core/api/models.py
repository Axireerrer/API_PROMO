from django.db import models


# Модель объявления
class Advert(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок объявления')
    advert_id = models.IntegerField(unique=True, verbose_name='ID')
    author = models.CharField(max_length=100, verbose_name='Автор объявления')
    views_count = models.IntegerField(verbose_name='Количество просмотров')
    position = models.IntegerField(verbose_name='Позиция объявления', null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
