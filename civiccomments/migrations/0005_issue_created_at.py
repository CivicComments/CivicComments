# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-16 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civiccomments', '0004_auto_20181116_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
