# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0004_auto_20190317_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('number', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]
