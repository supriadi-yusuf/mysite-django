# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-05 22:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('modelform_app', '0006_auto_20190605_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 5, 22, 48, 10, 47544, tzinfo=utc), editable=False),
        ),
    ]