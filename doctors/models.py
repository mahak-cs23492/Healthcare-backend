from django.db import models


class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('Dermatology', 'Dermatology'),
        ('Psychiatry', 'Psychiatry'),
        ('Oncology', 'Oncology'),
        ('Radiology', 'Radiology'),
        ('General Medicine', 'General Medicine'),
        ('Surgery', 'Surgery'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    hospital = models.CharField(max_length=255, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'doctors'
        ordering = ['-created_at']

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"
