# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='weburl',
            field=models.URLField(max_length=1000, verbose_name='weburl'),
        ),
    ]
