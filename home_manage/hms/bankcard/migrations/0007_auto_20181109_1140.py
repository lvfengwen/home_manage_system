# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-09 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankcard', '0006_auto_20181109_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='银行')),
            ],
        ),
        migrations.RenameField(
            model_name='bankcardinfo',
            old_name='card_num',
            new_name='bankcard_num',
        ),
        migrations.RemoveField(
            model_name='bankcardinfo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='bankcardinfo',
            name='type',
        ),
        migrations.AddField(
            model_name='bankcardinfo',
            name='bankcard_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bankcardinfo_banktype', to='bankcard.BankCardType', verbose_name='银行卡类型'),
        ),
        migrations.AddField(
            model_name='bankcardinfo',
            name='bank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bankcardinfo_bank', to='bankcard.Bank', verbose_name='银行'),
        ),
    ]