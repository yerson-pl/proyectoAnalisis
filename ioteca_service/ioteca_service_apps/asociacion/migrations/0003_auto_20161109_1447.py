# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-09 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asociacion', '0002_lote_socio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informacionlote',
            name='informacion_lote',
        ),
        migrations.AlterModelOptions(
            name='sociolote',
            options={'verbose_name': 'Relacion de socio a lote', 'verbose_name_plural': 'Relacion de socio a lotes'},
        ),
        migrations.AddField(
            model_name='sociolote',
            name='area_construida',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='sociolote',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sociolote',
            name='estado_inmueble',
            field=models.CharField(blank=True, choices=[('Terreno sin construir', 'Terreno sin construir'), ('Terreno con cerco perimetrico', 'Terreno con cerco perimetrico'), ('Inmueble parcialmente construido', 'Inmueble parcialmente construido'), ('Inmueble construido - primera planta', 'Inmueble construido - primera planta'), ('Inmueble construido - segunda planta', 'Inmueble construido - segunda planta'), ('Inmueble construido - más de dos plantas', 'Inmueble construido - más de dos plantas')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='sociolote',
            name='observaciones',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='InformacionLote',
        ),
    ]
