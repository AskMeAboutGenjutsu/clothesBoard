# Generated by Django 4.0.5 on 2022-07-09 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accoutUser', '0005_alter_userprofilemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='city',
            field=models.CharField(default='Неизвестный город', max_length=20, verbose_name='Город пользователя'),
        ),
    ]