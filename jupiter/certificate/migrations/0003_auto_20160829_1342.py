# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-29 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0002_auto_20160829_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivatecertificate',
            name='issued_by',
            field=models.CharField(choices=[('W1', 'Wrapdigi Authority W1'), ('W2', 'Wrapdigi Authority W2')], default=1, max_length=20, verbose_name='Issued By'),
        ),
    ]
