# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 19:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authtools', '0003_auto_20160212_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('title', models.CharField(max_length=120)),
                ('docfile', models.FileField(blank=True, null=True, upload_to='Product/%Y/%m/%d')),
                ('description', models.CharField(default=False, max_length=160)),
                ('active', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(default=0)),
                ('zip_Code', models.CharField(blank=True, max_length=6)),
                ('address', models.CharField(default=False, max_length=60)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_Update', models.DateTimeField(default=django.utils.timezone.now)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('docfile',),
                'verbose_name': 'Product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
