# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
