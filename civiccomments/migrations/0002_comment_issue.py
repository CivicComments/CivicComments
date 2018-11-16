# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-11 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('civiccomments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='civiccomments.Issue'),
            preserve_default=False,
        ),
    ]
