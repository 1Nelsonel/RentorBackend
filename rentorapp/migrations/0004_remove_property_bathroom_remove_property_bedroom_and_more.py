# Generated by Django 4.0.5 on 2023-02-08 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentorapp', '0003_remove_property_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='bathroom',
        ),
        migrations.RemoveField(
            model_name='property',
            name='bedroom',
        ),
        migrations.RemoveField(
            model_name='property',
            name='category',
        ),
        migrations.RemoveField(
            model_name='property',
            name='garage',
        ),
    ]
