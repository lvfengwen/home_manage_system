# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-14 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiction', '0007_fictioninfo_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fictioninfo',
            name='source',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='资源来源'),
        ),
    ]
