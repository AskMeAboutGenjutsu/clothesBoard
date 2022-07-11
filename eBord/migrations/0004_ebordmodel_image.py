# Generated by Django 4.0.5 on 2022-07-02 18:50

from django.db import migrations, models
import eBord.models


class Migration(migrations.Migration):

    dependencies = [
        ('eBord', '0003_alter_ebordmodel_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebordmodel',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to=eBord.models.get_timestamp_path, verbose_name='Изображение товара'),
        ),
    ]