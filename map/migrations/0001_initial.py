# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 08:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import map.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calibration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='im_height', upload_to=map.models.calib_image_name, verbose_name='Map Image', width_field='im_width')),
                ('im_height', models.PositiveIntegerField(verbose_name='Height')),
                ('im_width', models.PositiveIntegerField(verbose_name='Width')),
            ],
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=1000, verbose_name='Location')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('gps_la', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitude')),
                ('gps_lo', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitude')),
                ('height', models.PositiveIntegerField(verbose_name='Height')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2000, verbose_name='Description')),
                ('floor', models.IntegerField(default=0, verbose_name='Floor')),
                ('image', models.ImageField(height_field='im_height', upload_to=map.models.map_file_name, verbose_name='Map Image', width_field='im_width')),
                ('im_height', models.PositiveIntegerField(editable=False, verbose_name='Height')),
                ('im_width', models.PositiveIntegerField(editable=False, verbose_name='Width')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
            ],
        ),
        migrations.AddField(
            model_name='camera',
            name='map_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.Map'),
        ),
    ]
