# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-21 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('vk_id', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Adept', 'Adept'), ('User', 'User')], default='User', max_length=5)),
                ('about', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
