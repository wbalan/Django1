# Generated by Django 4.1.7 on 2023-03-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='number',
            field=models.PositiveSmallIntegerField(unique=True, verbose_name='Номер'),
        ),
    ]
