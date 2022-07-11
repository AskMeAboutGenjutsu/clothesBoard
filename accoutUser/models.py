from django.db import models
from django.contrib.auth.models import User
from os.path import splitext
from PIL import Image


def get_user_img_name(instance, filename):
    return f'user_{splitext(filename)}'


class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фото пользователя', upload_to=get_user_img_name, default='default_user.png')
    city = models.CharField(verbose_name='Город пользователя', max_length=20, default='Неизвестный город')

    def __str__(self):
        return f'Профиль пользователя {self.user}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        img = Image.open(self.image.path)
        if img.height >= 256 or img.width >= 256:
            resize = (256, 256)
            img.thumbnail(resize)
            img.save(self.image.path)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
