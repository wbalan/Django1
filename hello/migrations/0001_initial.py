# Generated by Django 4.1.7 on 2023-03-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(max_length=12, unique=True, verbose_name='Номер')),
                ('description', models.TextField()),
            ],
        ),
    ]