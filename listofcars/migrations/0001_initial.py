# Generated by Django 4.2 on 2024-11-12 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('carid', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=255, verbose_name='Марка')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('description', models.TextField(verbose_name='описание автомобиля')),
                ('is_reserved', models.BooleanField(default=False)),
                ('cost_per_hour', models.IntegerField(verbose_name='Стоимость за час')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата и время последнего обновления записи')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('counthours', models.IntegerField(verbose_name='Кол часов')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contract_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Контракт',
                'verbose_name_plural': 'Контракты',
            },
        ),
    ]
