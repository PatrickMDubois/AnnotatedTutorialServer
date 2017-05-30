# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-26 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0011_note_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='num_ratings',
            field=models.CharField(blank=True, default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='note',
            name='rating',
            field=models.CharField(blank=True, default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='note',
            name='type',
            field=models.CharField(blank=True, default='suggestion', max_length=50),
        ),
    ]
