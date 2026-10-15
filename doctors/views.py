from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorListCreateView(APIView):
    """
    GET  /api/doctors/ - Retrieve all doctors.
    POST /api/doctors/ - Add a new doctor (authenticated users only).
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(
            {
                'count': doctors.count(),
                'doctors': serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Doctor created successfully.',
                    'doctor': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class DoctorDetailView(APIView):
    """
    GET    /api/doctors/<id>/ - Retrieve a specific doctor.
    PUT    /api/doctors/<id>/ - Update doctor details.
    DELETE /api/doctors/<id>/ - Delete a doctor record.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Doctor updated successfully.',
                    'doctor': serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response(
            {'message': 'Doctor deleted successfully.'},
            status=status.HTTP_200_OK
        )
