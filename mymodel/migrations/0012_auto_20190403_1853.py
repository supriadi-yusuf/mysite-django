# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0011_auto_20190403_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ox',
            options={'ordering': ['horn_length'], 'verbose_name_plural': 'Oxen'},
        ),
    ]
