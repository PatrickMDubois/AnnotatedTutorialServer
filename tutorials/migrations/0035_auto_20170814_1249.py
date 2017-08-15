# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-14 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0034_contributor_current_tutorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tutorial_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='tutorials.Tutorial'),
        ),
    ]