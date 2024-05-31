# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-01-23 07:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0623_auto_20230717_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='offence',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offence_district', to='wildlifecompliance.District'),
        ),
        migrations.AddField(
            model_name='offence',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offence_region', to='wildlifecompliance.Region'),
        ),
        migrations.AlterField(
            model_name='sanctionoutcome',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('awaiting_endorsement', 'Awaiting Endorsement'), ('awaiting_payment', 'Awaiting Payment'), ('awaiting_print_and_post', 'Awaiting Print and Post'), ('with_dot', 'With Dep. of Transport'), ('awaiting_review', 'Awaiting Review'), ('awaiting_issuance', 'Awaiting Issuance'), ('awaiting_remediation_actions', 'Awaiting Remediation Actions'), ('escalated_for_withdrawal', 'Escalated for Withdrawal'), ('declined', 'Declined'), ('overdue', 'Overdue'), ('withdrawn', 'Withdrawn'), ('closed', 'Closed')], default='draft', max_length=40),
        ),
    ]