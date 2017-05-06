# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-29 13:19
from __future__ import unicode_literals

import certificate.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(default='Standard SSL', max_length=200, verbose_name='Certificate Name')),
                ('status', models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=1, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='CertificateDuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(default=1, verbose_name='Duration (Years)')),
                ('cost', models.IntegerField(default=20, verbose_name='Cost')),
                ('status', models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=1, verbose_name='Status')),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate.Certificate')),
            ],
        ),
        migrations.CreateModel(
            name='UserActivateCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_text', models.TextField(verbose_name='Certificate')),
                ('issued_by', models.TextField(max_length=20, verbose_name='Issued By')),
                ('issued_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Issued Date')),
                ('expired_date', models.DateTimeField(verbose_name='Expired Date')),
                ('status', models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=1, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='UserCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(default=certificate.models.get_random_uuid, max_length=20, verbose_name='Certificate Number')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
                ('activate', models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Activate')),
                ('status', models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=1, verbose_name='Status')),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate.CertificateDuration')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='useractivatecertificate',
            name='certificate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate.UserCertificate'),
        ),
    ]
