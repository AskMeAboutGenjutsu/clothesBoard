# Generated by Django 4.0.5 on 2022-07-04 11:19

from django.db import migrations, models
import eBord.models


class Migration(migrations.Migration):

    dependencies = [
        ('eBord', '0007_alter_categorymodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebordmodel',
            name='image',
            field=models.ImageField(default='ads/default.jpeg', upload_to=eBord.models.get_timestamp_path, verbose_name='Изображение товара'),
        ),
    ]
