# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-13 03:51
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
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='作者名')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='书名')),
                ('word_count', models.FloatField(blank=True, null=True, verbose_name='字数（万字）')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='book_author', to='reading.Author', verbose_name='作者')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='国家')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='语言')),
            ],
        ),
        migrations.CreateModel(
            name='ReadingPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='计划名称')),
                ('start_datetime', models.DateTimeField(verbose_name='开始时间')),
                ('end_datetime', models.DateTimeField(verbose_name='截至时间')),
                ('overdue_day', models.IntegerField(default=0, verbose_name='逾期天数')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('book', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='readingplan_book', to='reading.Book', verbose_name='图书')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='readingplan_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('mender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='readingplan_mender', to=settings.AUTH_USER_MODEL, verbose_name='修改者')),
            ],
        ),
        migrations.CreateModel(
            name='ReadingSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_count', models.IntegerField(default=0, verbose_name='图书数量')),
                ('language_count', models.IntegerField(default=1, verbose_name='语言计数')),
                ('word_count', models.FloatField(default=0, verbose_name='总字数（万字）')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='readingsummary_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('mender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='readingsummary_mender', to=settings.AUTH_USER_MODEL, verbose_name='修改者')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='状态名称')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='标签')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tag_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('mender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tag_mender', to=settings.AUTH_USER_MODEL, verbose_name='修改者')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='类型名称')),
            ],
        ),
        migrations.AddField(
            model_name='readingplan',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='readingplan_plan_status', to='reading.Status', verbose_name='计划状态'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='book_book_type', to='reading.Type', verbose_name='图书类型'),
        ),
        migrations.AddField(
            model_name='book',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='book_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='book_language', to='reading.Language', verbose_name='语言'),
        ),
        migrations.AddField(
            model_name='book',
            name='mender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='book_mender', to=settings.AUTH_USER_MODEL, verbose_name='修改者'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, to='reading.Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='author_country', to='reading.Country', verbose_name='国家'),
        ),
    ]
