# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-16 20:55


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civiccomments', '0005_issue_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='short_summary',
            field=models.TextField(default=b''),
        ),
    ]
