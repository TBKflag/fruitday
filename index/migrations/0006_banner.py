# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-07 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20180503_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='banner')),
                ('picture', models.ImageField(upload_to='staic/upload/banner', verbose_name='图片')),
            ],
        ),
    ]
