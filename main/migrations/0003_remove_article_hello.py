# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-12 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_hello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hello',
        ),
    ]
