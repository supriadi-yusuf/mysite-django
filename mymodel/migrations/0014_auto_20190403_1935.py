# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0013_base1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(related_name='mymodel_base_related', related_query_name='mymodel_bases', to='mymodel.Country')),
            ],
        ),
        migrations.RemoveField(
            model_name='base1',
            name='members',
        ),
        migrations.DeleteModel(
            name='Base1',
        ),
    ]
