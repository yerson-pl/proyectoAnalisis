# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-15 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asociacion', '0003_auto_20161109_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociolote',
            name='nro_inasistencias',
            field=models.IntegerField(default=0),
        ),
    ]
