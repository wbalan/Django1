# Generated by Django 4.1.7 on 2023-03-31 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uchet', '0004_alter_journal_date_rep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='date_rep',
            field=models.DateField(blank=True, default=None),
        ),
    ]
