
from email.policy import default
from django.db import models
from django.utils import timezone
# from django.db import IntegrityError




class Patients(models.Model):
    patient_Name = models.CharField(max_length=100)
    dr_Name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=timezone.now)
    age = models.IntegerField()
    phone = models.CharField(max_length=70, default="")
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.patient_Name