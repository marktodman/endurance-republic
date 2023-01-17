# Generated by Django 3.2 on 2023-01-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
