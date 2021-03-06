# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-15 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0037_note_tutorial_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='category',
        ),
        migrations.RemoveField(
            model_name='note',
            name='content',
        ),
        migrations.RemoveField(
            model_name='note',
            name='contributor',
        ),
        migrations.RemoveField(
            model_name='note',
            name='contributor_list',
        ),
        migrations.RemoveField(
            model_name='note',
            name='dateSubmitted',
        ),
        migrations.RemoveField(
            model_name='note',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='note',
            name='extra_info',
        ),
        migrations.RemoveField(
            model_name='note',
            name='reply_to',
        ),
        migrations.RemoveField(
            model_name='note',
            name='tutorial_id',
        ),
        migrations.RemoveField(
            model_name='note',
            name='user_submitted',
        ),
        migrations.AlterField(
            model_name='note',
            name='step_id',
            field=models.ManyToManyField(blank=True, null=True, related_name='notes', to='tutorials.Step'),
        ),
    ]
