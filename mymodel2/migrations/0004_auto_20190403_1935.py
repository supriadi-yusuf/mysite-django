# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel2', '0003_base2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='base2',
            name='members',
        ),
        migrations.DeleteModel(
            name='Base2',
        ),
    ]
