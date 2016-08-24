# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='name')),
                ('content', models.TextField(verbose_name='content')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('id_num', models.IntegerField(verbose_name='id_num')),
                ('birth', models.DateField(verbose_name='birth')),
            ],
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=40, verbose_name='name')),
                ('device_ip', models.CharField(max_length=20, verbose_name='device_ip')),
                ('weburl', models.CharField(max_length=1000, verbose_name='weburl')),
                ('page_content', models.TextField(verbose_name='page_content')),
            ],
        ),
    ]