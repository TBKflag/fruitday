# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-07 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='picture',
            field=models.ImageField(upload_to='index/static/upload/banner', verbose_name='图片'),
        ),
    ]