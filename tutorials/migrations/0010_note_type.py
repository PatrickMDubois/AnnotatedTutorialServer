# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-16 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0009_step_step_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]