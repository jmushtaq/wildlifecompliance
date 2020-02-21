# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-02-19 02:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wildlifecompliance', '0431_merge_20200218_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProsecutionBriefDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('_file', models.FileField(max_length=255, upload_to=b'')),
                ('input_name', models.CharField(blank=True, max_length=255, null=True)),
                ('can_delete', models.BooleanField(default=True)),
                ('version_comment', models.CharField(blank=True, max_length=255, null=True)),
                ('prosecution_brief', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='wildlifecompliance.ProsecutionBrief')),
            ],
        ),
        migrations.CreateModel(
            name='ProsecutionBriefOtherStatements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticked', models.BooleanField(default=False)),
                ('associated_doc_artifact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_artifact_pb_other_statements', to='wildlifecompliance.DocumentArtifact')),
                ('children', models.ManyToManyField(related_name='parents', to='wildlifecompliance.ProsecutionBriefOtherStatements')),
                ('legal_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='legal_case_pb_other_statements', to='wildlifecompliance.LegalCase')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_user_pb_other_statements', to=settings.AUTH_USER_MODEL)),
                ('statement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statement_pb_other_statements', to='wildlifecompliance.DocumentArtifact')),
            ],
        ),
        migrations.CreateModel(
            name='ProsecutionBriefRecordOfInterview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticked', models.BooleanField(default=False)),
                ('associated_doc_artifact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_artifact_pb_roi', to='wildlifecompliance.DocumentArtifact')),
                ('children', models.ManyToManyField(related_name='parents', to='wildlifecompliance.ProsecutionBriefRecordOfInterview')),
                ('legal_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='legal_case_pb_roi', to='wildlifecompliance.LegalCase')),
                ('offence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offence_pb_roi', to='wildlifecompliance.Offence')),
                ('offender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offender_pb_roi', to='wildlifecompliance.Offender')),
                ('record_of_interview', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='record_of_interview_pb_roi', to='wildlifecompliance.DocumentArtifact')),
            ],
        ),
    ]
