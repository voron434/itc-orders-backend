# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 00:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20180125_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
