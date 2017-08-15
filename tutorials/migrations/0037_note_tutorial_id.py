# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-15 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0036_remove_note_tutorial_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tutorial_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='tutorials.Tutorial'),
        ),
    ]