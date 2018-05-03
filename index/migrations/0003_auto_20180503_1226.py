# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-03 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180503_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='启用'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='picture',
            field=models.ImageField(upload_to='static/upload/goods', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='spec',
            field=models.CharField(max_length=30, verbose_name='介绍'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.CharField(max_length=30, verbose_name='商品类别'),
        ),
    ]
