# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-25 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_auto_20160524_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tutorial_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='tutorials.Tutorial'),
            preserve_default=False,
        ),
    ]
