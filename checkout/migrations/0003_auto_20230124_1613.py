# Generated by Django 3.2 on 2023-01-24 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_emergency_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
    ]
