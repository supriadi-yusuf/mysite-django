# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-03 04:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('modelform_app', '0011_auto_20190703_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 3, 4, 0, 39, 402755, tzinfo=utc), editable=False),
        ),
    ]