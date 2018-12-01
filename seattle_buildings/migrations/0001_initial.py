# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-02 02:20


import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeattleLandUsePermitDoc',
            fields=[
                ('document_id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('url', models.TextField()),
                ('land_use_id', models.TextField()),
                ('date', models.DateField()),
                ('is_text_machine_readable', models.NullBooleanField(default=None)),
                ('text', models.TextField(blank=True, null=True)),
                ('structured_data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
