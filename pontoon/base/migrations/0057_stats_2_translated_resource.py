# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0056_auto_20160217_1742'),
    ]

    operations = [
        migrations.RenameModel('Stats', 'TranslatedResource'),
    ]
