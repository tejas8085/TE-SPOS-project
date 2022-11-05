from http.client import HTTPResponse
from django.shortcuts import render
from dashboard.models import Patients
import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'dashboard/index.html')
def Base(request):
    return render(request, 'dashboard/basic.html')
# def ADD_PATIENT(request):
#     return render(request,'dashboard/patient/add_patient.html')

def ADD_PATIENT(request):
    patient_name=""
    age=""
    dob=""
    address=""
    phone=""
    dr_name=""
    if request.method == "POST":
       
        patient_name = request.POST.get('patient_name')
        dr_name = request.POST.get('dr_name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        patient = Patients(
            
            patient_Name = patient_name,
            dr_Name = dr_name,
            date_of_birth = dob,
            age = age,
            phone = phone,
            gender = gender,
            email = email,
            address = address,
        )
        patient.save()

    return render(request,'dashboard/patient/add_patient.html', {'patient_name':patient_name, 'age':age, 'phone':phone, 'address':address, 'dr_Name':dr_name , 'date_of_birth':dob })
    # return render(request , {'patient_name':patient_name, 'age':age, 'phone':phone, 'address':address, 'dr_Name':dr_name , 'date_of_birth':dob })
    
   




def ALL_PATIENT(request):
    # patient_name:global
    
        return render(request,'dashboard/patient/patients_all.html' )
    
    
