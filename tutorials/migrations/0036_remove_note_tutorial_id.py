# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-15 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0035_auto_20170814_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='tutorial_id',
        ),
    ]
