# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-10 07:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel2', '0014_childb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childb',
            name='ancestor',
        ),
        migrations.DeleteModel(
            name='ChildB',
        ),
    ]