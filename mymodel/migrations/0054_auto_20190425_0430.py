# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-25 04:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0053_auto_20190425_0323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]
