from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from os.path import splitext
from PIL import Image


def get_timestamp_path(instance, filename):
    return f'{instance.author}_{datetime.now()}{splitext(filename)[1]}'


class EBordModel(models.Model):
    title = models.CharField(verbose_name='Название товара', max_length=15, null=False, blank=False)
    content = models.TextField(verbose_name='Описание товара', null=False, blank=False)
    price = models.DecimalField(verbose_name='Цена товара', max_digits=6, decimal_places=2)
    date = models.DateTimeField(verbose_name='Дата создания объявления', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey('CategoryModel', on_delete=models.PROTECT, verbose_name='Категория товара', default='Футболка')
    image = models.ImageField(verbose_name='Изображение товара', upload_to=get_timestamp_path, default='default.jpeg')

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            resize = (400, 400)
            img.thumbnail(resize)
            img.save(self.image.path)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-date', 'author']


def get_categories_filename(instance, filename):
    return f'{instance.name}{splitext(filename)[1]}'


class CategoryModel(models.Model):
    name = models.CharField(verbose_name='Категория товара', max_length=15, primary_key=True)
    image = models.ImageField(
        verbose_name='Изображение товара', upload_to=get_categories_filename, default='default.jpeg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['name']