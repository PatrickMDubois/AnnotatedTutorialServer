# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-03 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='author',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='software',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
