# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 05:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InternetAccountInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='账号名称')),
                ('account', models.CharField(max_length=100, verbose_name='账号')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('random_salt', models.CharField(blank=True, max_length=100, null=True, verbose_name='随机盐值')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('total', models.FloatField(verbose_name='交易金额')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='internetaccountinfo_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('mender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='internetaccountinfo_mender', to=settings.AUTH_USER_MODEL, verbose_name='修改者')),
            ],
        ),
        migrations.CreateModel(
            name='SaltValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='盐值')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='saltvalue_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('mender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='saltvalue_mender', to=settings.AUTH_USER_MODEL, verbose_name='修改者')),
            ],
        ),
    ]
