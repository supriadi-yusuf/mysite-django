# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-03 03:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('modelform_app', '0009_auto_20190620_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 3, 3, 59, 38, 28889, tzinfo=utc), editable=False),
        ),
    ]
