# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-14 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiction', '0006_remove_fictioninfo_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='fictioninfo',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='fictioninfo_author', to='fiction.Author', verbose_name='作者'),
        ),
    ]