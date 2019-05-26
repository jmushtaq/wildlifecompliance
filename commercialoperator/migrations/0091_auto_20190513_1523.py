# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-05-13 07:23
from __future__ import unicode_literals

import commercialoperator.components.compliances.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0090_merge_20190513_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['name'], 'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='activitycategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'Activity Categories'},
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='applicant',
        ),
        migrations.AddField(
            model_name='proposal',
            name='org_applicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_applications', to='commercialoperator.Organisation'),
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(upload_to=commercialoperator.components.compliances.models.update_proposal_complaince_filename),
        ),
    ]