# Generated by Django 4.0.5 on 2022-07-05 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accoutUser', '0002_rename_userprofile_userprofilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='image',
            field=models.ImageField(default='default_user.png', upload_to='user_img', verbose_name='Фото пользователя'),
        ),
    ]