# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 02:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0005_mobile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mobile',
        ),
    ]
