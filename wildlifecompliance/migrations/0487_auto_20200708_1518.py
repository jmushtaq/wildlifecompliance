# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-08 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0486_auto_20200708_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='licencepurpose',
            name='amendment_fee',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=8),
        ),
        migrations.AddField(
            model_name='licencepurpose',
            name='renewal_fee',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=8),
        ),
    ]
