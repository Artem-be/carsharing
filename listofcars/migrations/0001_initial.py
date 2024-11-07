# Generated by Django 5.1.3 on 2024-11-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carid', models.IntegerField(unique=True, verbose_name='ID')),
                ('make', models.CharField(max_length=255, verbose_name='Марка')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('description', models.TextField(verbose_name='описание автомобиля')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата и время последнего обновления записи')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
