# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-01-15 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0380_physicalartifact_custodian_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='legalcase',
            name='accused_bad_character',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='accused_bad_character_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='applications_orders_requests',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='applications_orders_requests_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='applications_orders_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='applications_orders_required_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='further_persons_interviews_pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='further_persons_interviews_pending_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='local_public_interest',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='local_public_interest_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='other_interviews',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='other_interviews_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='other_legal_matters',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='other_legal_matters_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='other_persons_receiving_sanction_outcome',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='other_persons_receiving_sanction_outcome_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='problems_needs_prosecution_witnesses',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='problems_needs_prosecution_witnesses_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='relevant_persons_pending_charges',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='relevant_persons_pending_charges_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='statements_pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='statements_pending_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='victim_impact_statement_taken',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='victim_impact_statement_taken_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='vulnerable_hostile_witnesses',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='vulnerable_hostile_witnesses_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='witness_refusing_statement',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='witness_refusing_statement_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]