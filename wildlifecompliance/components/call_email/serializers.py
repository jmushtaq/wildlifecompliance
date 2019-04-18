import traceback
from wildlifecompliance.components.call_email.models import (
    CallEmail,
    Classification,
    ReportType,
    ComplianceFormDataRecord,
)
from wildlifecompliance.components.applications.serializers import BaseApplicationSerializer
from rest_framework import serializers
from django.core.exceptions import ValidationError


class ComplianceFormDataRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceFormDataRecord
        fields = (
            'field_name',
            'schema_name',
            'component_type',
            'instance_name',
            'comment',
            'deficiency',
            'value',
        )
        read_only_fields = (
            'field_name',
            'schema_name',
            'component_type',
            'instance_name',
            'comment',
            'deficiency',
            'value',
        )


class ClassificationSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='get_name_display')

    class Meta:
        model = Classification
        fields = (
            'id',
            'name',
        )
        read_only_fields = ('id', 'name', )


class CreateCallEmailSerializer(serializers.ModelSerializer):
    data = ComplianceFormDataRecordSerializer(many=True)

    class Meta:
        model = CallEmail
        fields = (
            'id',
            'status',
            'classification',
            'number',
            'caller',
            'assigned_to',
            'data',
        )
        read_only_fields = ('id', )


class ReportTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportType
        fields = (
            'report_type',
            'schema',
        )
        read_only_fields = ('report_type', 'schema')


class CallEmailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    classification = ClassificationSerializer()
    lodgement_date = serializers.CharField(
        source='lodged_on')
    report_type = ReportTypeSerializer()
    data = ComplianceFormDataRecordSerializer(many=True)

    class Meta:
        model = CallEmail
        fields = (
            'id',
            'status',
            'location',
            'classification',
            'schema',
            'lodgement_date',
            'number',
            'caller',
            'assigned_to',
            'report_type',
            'data',
        )
        read_only_fields = ('id', )


class UpdateRendererDataSerializer(CallEmailSerializer):
    data = ComplianceFormDataRecordSerializer(many=True)

    class Meta:
        model = CallEmail
        fields = (
            'schema',
            'data',
        )
