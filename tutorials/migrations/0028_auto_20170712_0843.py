# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-12 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0027_auto_20170705_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='tutorial_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutorialOne', to='tutorials.Tutorial'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='tutorial_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutorialThree', to='tutorials.Tutorial'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='tutorial_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutorialTwo', to='tutorials.Tutorial'),
        ),
    ]
