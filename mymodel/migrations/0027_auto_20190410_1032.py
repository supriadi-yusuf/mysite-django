# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-10 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel2', '0017_auto_20190410_1032'),
        ('mymodel', '0026_ancestor_childa_childb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childa',
            name='ancestors',
        ),
        migrations.RemoveField(
            model_name='childb',
            name='ancestors',
        ),
        migrations.DeleteModel(
            name='Ancestor',
        ),
        migrations.DeleteModel(
            name='ChildA',
        ),
        migrations.DeleteModel(
            name='ChildB',
        ),
    ]
