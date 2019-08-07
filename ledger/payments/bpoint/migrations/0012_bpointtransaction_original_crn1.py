# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-07 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpoint', '0011_auto_20171026_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='bpointtransaction',
            name='original_crn1',
            field=models.CharField(blank=True, help_text='Reference for the order that the transaction was made for', max_length=50, null=True),
        ),
    ]
