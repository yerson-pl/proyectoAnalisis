# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-09 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asociacion', '0003_auto_20161109_1447'),
        ('eventos', '0008_auto_20161103_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='lote',
        ),
        migrations.AddField(
            model_name='asistencia',
            name='socio_lote',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='asociacion.SocioLote'),
            preserve_default=False,
        ),
    ]
