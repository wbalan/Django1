# Generated by Django 4.1.7 on 2023-03-20 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_remove_routesheet_dateoperation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routesheet',
            name='charge',
        ),
        migrations.RemoveField(
            model_name='routesheet',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='routesheet',
            name='kindofoperation',
        ),
        migrations.RemoveField(
            model_name='routesheet',
            name='running',
        ),
        migrations.RemoveField(
            model_name='routesheet',
            name='stateout',
        ),
    ]