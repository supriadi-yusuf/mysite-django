# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-25 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0051_auto_20190424_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='num_awards',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='store',
            name='registered_user',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
