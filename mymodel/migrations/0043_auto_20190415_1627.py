# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-15 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0042_auto_20190415_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mod_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
