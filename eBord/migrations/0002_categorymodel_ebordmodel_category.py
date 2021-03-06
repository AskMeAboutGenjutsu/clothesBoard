# Generated by Django 4.0.5 on 2022-06-24 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eBord', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('name', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='ebordmodel',
            name='category',
            field=models.ForeignKey(default='Футболка', on_delete=django.db.models.deletion.PROTECT, to='eBord.categorymodel', verbose_name='Категория товара'),
        ),
    ]
