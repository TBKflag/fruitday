# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-03 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180503_1226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodstype',
            options={'verbose_name': '商品类别', 'verbose_name_plural': '商品类别'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterModelTable(
            name='goodstype',
            table='goodsytpe',
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]
