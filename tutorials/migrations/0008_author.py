# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-14 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0007_auto_20160530_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('current_tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_access', to='tutorials.Tutorial')),
            ],
        ),
    ]
