# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-06-03 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_mess', '0008_auto_20200522_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_bill',
            name='month',
            field=models.CharField(default=6, max_length=20),
        ),
    ]
