# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankcard', '0004_bankcardinfo_card_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankcardinfo',
            name='card_num',
            field=models.CharField(max_length=100, verbose_name='银行卡号'),
        ),
    ]
