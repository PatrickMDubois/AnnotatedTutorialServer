# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-30 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0015_remove_note_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Contributor',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='author',
            new_name='contributor',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='author',
            new_name='contributor',
        ),
    ]
