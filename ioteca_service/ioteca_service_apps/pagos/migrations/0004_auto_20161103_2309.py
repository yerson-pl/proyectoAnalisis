# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-03 23:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0003_periodo_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='creacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 3, 23, 9, 40, 74322, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='pago',
            name='modificacion',
            field=models.DateField(default=datetime.datetime(2016, 11, 3, 23, 9, 40, 74373)),
        ),
    ]
