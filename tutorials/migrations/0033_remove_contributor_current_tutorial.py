# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-14 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0032_auto_20170810_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='current_tutorial',
        ),
    ]
