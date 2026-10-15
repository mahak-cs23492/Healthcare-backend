from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Patient
        fields = (
            'id', 'name', 'age', 'gender', 'blood_group',
            'phone', 'address', 'medical_history',
            'created_by', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def validate_age(self, value):
        if value <= 0 or value > 150:
            raise serializers.ValidationError("Age must be between 1 and 150.")
        return value
