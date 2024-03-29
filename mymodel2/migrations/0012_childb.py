# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-09 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mymodel', '0022_childa_childb'),
        ('mymodel2', '0011_auto_20190409_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('members', models.ManyToManyField(related_name='mymodel2_childb_related', related_query_name='mymodel2_childbs', to='mymodel.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
