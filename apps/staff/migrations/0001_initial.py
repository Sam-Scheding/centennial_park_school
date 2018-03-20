# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-26 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('blurb', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'staff',
                'verbose_name_plural': 'staff',
            },
        ),
    ]
