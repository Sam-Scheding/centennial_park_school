# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 23:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryimage',
            old_name='blob',
            new_name='image',
        ),
    ]
