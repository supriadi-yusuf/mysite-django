# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-23 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0047_auto_20190418_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mymodel.Entry')),
            ],
        ),
    ]
