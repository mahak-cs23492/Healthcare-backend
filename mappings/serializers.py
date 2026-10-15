from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


class MappingSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = (
            'id', 'patient', 'doctor', 'notes', 'assigned_at',
            'patient_details', 'doctor_details'
        )
        read_only_fields = ('id', 'assigned_at')

    def validate(self, data):
        patient = data.get('patient')
        doctor = data.get('doctor')
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to this patient."
            )
        return data
