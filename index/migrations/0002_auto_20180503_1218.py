# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-03 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterModelTable(
            name='goods',
            table='goods',
        ),
    ]