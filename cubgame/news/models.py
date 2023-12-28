from django.contrib.auth.models import AbstractUser
from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    dost = models.CharField('Имя пользователя', max_length=250)
    full_text = models.TextField('Статья', max_length=250)
    fault = models.TextField("Недостатки", max_length=255)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
