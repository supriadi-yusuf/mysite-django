# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-09 02:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel2', '0006_auto_20190409_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child2',
            name='base_ptr',
        ),
        migrations.DeleteModel(
            name='Child2',
        ),
    ]
