from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('hospital', 'Hospital'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name