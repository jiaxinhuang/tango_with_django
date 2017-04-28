# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-27 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
