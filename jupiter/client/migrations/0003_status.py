# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-12 13:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0002_auto_20170212_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_messages', models.TextField(verbose_name='Status')),
                ('read_status', models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=1, verbose_name='Read_Status')),
                ('status', models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=1, verbose_name='Status')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_status', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
