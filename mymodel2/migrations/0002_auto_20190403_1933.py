# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='base2',
            name='base1_ptr',
        ),
        migrations.DeleteModel(
            name='Base2',
        ),
    ]