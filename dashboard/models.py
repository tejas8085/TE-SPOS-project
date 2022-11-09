
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
    
    
    
    
class Doctor(models.Model):
   
    dr_Name = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=timezone.now)
    age = models.IntegerField()
    phone = models.CharField(max_length=70, default="")
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.dr_Name
    
    


class Appointment(models.Model):
   
    Patient_id = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    appointment_date = models.DateField(default=timezone.now)
    #  = models.DateTimeField()
    time_slot = models.CharField(max_length=70, default="")
    # email = models.EmailField(max_length=100)
    # gender = models.CharField(max_length=50)
    problem = models.TextField()

    def __str__(self):
        return self.patient_name
    
    
class Invoice(models.Model):
   
    Patient_id = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    addmission_date = models.DateField(default=timezone.now)
    discharge_date = models.DateField(default=timezone.now)
    cost = models.CharField(max_length=100)
    advance = models.CharField(max_length=100)
    pending = models.CharField(max_length=100)
   

    def __str__(self):
        return self.patient_name
       