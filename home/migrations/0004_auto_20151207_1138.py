# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20151207_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='original_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='end_date',
            field=models.DateField(verbose_name='date ends'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_date',
            field=models.DateField(auto_now_add=True, verbose_name='bid date'),
        ),
    ]
