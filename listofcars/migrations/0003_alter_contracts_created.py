# Generated by Django 4.2 on 2024-11-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listofcars', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
