# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 18:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobssubmitted',
            options={'verbose_name': 'Job Submitted', 'verbose_name_plural': 'Jobs Submitted'},
        ),
    ]