# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-09 02:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel2', '0005_base2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Base2',
            new_name='Child2',
        ),
    ]
