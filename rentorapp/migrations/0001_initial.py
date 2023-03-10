# Generated by Django 4.0.5 on 2023-02-08 08:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandLord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('bank', models.CharField(max_length=100, null=True)),
                ('airport', models.CharField(max_length=100, null=True)),
                ('school', models.CharField(max_length=300, null=True)),
                ('mapLink', models.URLField(max_length=2048, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Propertycategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('size', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('bedroom', models.IntegerField(default=0)),
                ('bathroom', models.IntegerField(default=0)),
                ('garage', models.IntegerField(default=0)),
                ('rent', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('units', models.IntegerField(default=0)),
                ('imageOne', models.ImageField(blank=True, null=True, upload_to='upload/property_images')),
                ('imageTwo', models.ImageField(blank=True, null=True, upload_to='upload/property_images')),
                ('description', models.TextField(null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rentorapp.propertycategory')),
                ('landlord', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rentorapp.landlord')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rentorapp.location')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
