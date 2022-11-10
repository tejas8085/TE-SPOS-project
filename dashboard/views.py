from http.client import HTTPResponse
from django.shortcuts import render
from dashboard.models import Patients, Doctor, Appointment, Invoice, Room
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

def Index(request):
    data = Appointment.objects.all()
    if request.method == "POST":
        
        Patient_id = request.POST.get('patient_id')
        patient_name = request.POST.get('patient_name')
        department = request.POST.get('department')
        doctor_name = request.POST.get('doctor_name')
        appointment_date = request.POST.get('appointment_date')
        time_slot = request.POST.get('time_slot')
        problem = request.POST.get('problem')
        
       
        
        data = Appointment(  Patient_id =Patient_id, patient_name = patient_name, department = department, doctor_name=doctor_name, appointment_date=appointment_date, time_slot=time_slot, problem= problem)
        
        data.save()
       

    return render(request,'dashboard/index.html', {"messages":data})

    # return render(request, 'dashboard/index.html')
# def Index(request):
#     data = Patients.objects.all()
#     if request.method == "POST":
        
#         patient_name = request.POST.get('patient_name')
#         dr_name = request.POST.get('dr_name')
#         dob = request.POST.get('dob')
#         age = request.POST.get('age')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         gender = request.POST.get('gender')
#         address = request.POST.get('address')
        
#         data = Patients(patient_Name = patient_name, dr_Name = dr_name, dob=dob,age=age, phone=phone, email= email, gender=gender, address=address)
        
#         data.save()
       

#     return render(request,'dashboard/index.html', {"messages":data})

# def ADD_PATIENT(request):
#     return render(request,'dashboard/patient/add_patient.html')


#  ADD Patients SECTION
def ADD_PATIENT(request):
    data = Patients.objects.all()
    if request.method == "POST":
        
        patient_name = request.POST.get('patient_name')
        dr_name = request.POST.get('dr_name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        data = Patients(patient_Name = patient_name, dr_Name = dr_name, date_of_birth=dob,age=age, phone=phone, email= email, gender=gender, address=address)
        
        data.save()
       

    return render(request,'dashboard/patient/add_patient.html', {"messages":data})

# ADD doctor SECTION
def ADD_DOCTOR(request):
    data = Doctor.objects.all()
    if request.method == "POST":
        
        education = request.POST.get('education')
        dr_name = request.POST.get('dr_name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        data = Doctor( education =education, dr_Name = dr_name, date_of_birth=dob,age=age, phone=phone, email= email, gender=gender, address=address)
        
        data.save()
       

    return render(request,'dashboard/doctor/add_doctor.html', {"messages":data})


# ADD APPOINTEMENT
def ADD_APPOINTMENT(request):
    data = Appointment.objects.all()
    if request.method == "POST":
        
        Patient_id = request.POST.get('patient_id')
        patient_name = request.POST.get('patient_name')
        department = request.POST.get('department')
        doctor_name = request.POST.get('doctor_name')
        appointment_date = request.POST.get('appointment_date')
        time_slot = request.POST.get('time_slot')
        problem = request.POST.get('problem')
        
        data = Appointment( Patient_id =Patient_id, patient_name = patient_name, department = department, doctor_name=doctor_name, appointment_date=appointment_date, time_slot=time_slot, problem= problem)
        
        data.save()
       

    return render(request,'dashboard/appointments/add_appoint.html', {"messages":data})



# ADD INVOICES SECTION
def ADD_INVOICE(request):
    data = Invoice.objects.all()
    if request.method == "POST":
        
        Patient_id = request.POST.get('patient_id')
        patient_name = request.POST.get('patient_name')
        department = request.POST.get('department')
        doctor_name = request.POST.get('doctor_name')
        addmission_date = request.POST.get('addmission_date')
        discharge_date = request.POST.get('discharge_date')
        cost = request.POST.get('cost')
        advance = request.POST.get('advance')
        pending = request.POST.get('pending')
        
        data = Invoice( Patient_id =Patient_id, patient_name = patient_name, department = department, doctor_name=doctor_name, addmission_date=addmission_date, discharge_date=discharge_date, cost= cost, advance=advance, pending=pending )
        
        data.save()
       

    return render(request,'dashboard/payment/add_invoice.html', {"messages":data})


# ROOM ADD SECTION
def ADD_ROOM(request):
    data = Room.objects.all()
    if request.method == "POST":
        
        Patient_id = request.POST.get('patient_id')
        patient_name = request.POST.get('patient_name')
        department = request.POST.get('department')
        doctor_name = request.POST.get('doctor_name')
        admission_date = request.POST.get('admission_date')
        discharge = request.POST.get('discharge')
        room_no = request.POST.get('room_no')
        room_type = request.POST.get('room_type')
       
        data = Room( Patient_id =Patient_id, patient_name = patient_name, department = department, doctor_name=doctor_name, admission_date=admission_date, discharge=discharge,room_no= room_no, room_type=room_type )
        
        data.save()
       

    return render(request,'dashboard/room/add_room.html', {"messages":data})




# ALL Patients SECTION
def ALL_PATIENT(request):
    data = Patients.objects.all()
    if request.method == "POST":
        
        patient_name = request.POST.get('patient_name')
        dr_name = request.POST.get('dr_name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        data = Patients(patient_Name = patient_name, dr_Name = dr_name, date_of_birth=dob,age=age, phone=phone, email= email, gender=gender, address=address)
        
        data.save()
       

    return render(request,'dashboard/patient/patients_all.html', {"messages":data})


# ALL DOCTORS SECTION
def ALL_DOCTOR(request):
    data = Doctor.objects.all()
    if request.method == "POST":
        
        
        dr_name = request.POST.get('dr_name')
        education = request.POST.get('education')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        data = Doctor(education =education, dr_Name = dr_name, date_of_birth=dob,age=age, phone=phone, email= email, gender=gender, address=address, )

        
        data.save()
       

    return render(request,'dashboard/doctor/doctor_all.html', {"messages":data})

# ALL APPOINRTMENT SECTION
def ALL_APPOINTMENT(request):
    data = Appointment.objects.all()
    if request.method == "POST":
        
        Patient_id = request.POST.get('patient_id')
        department = request.POST.get('department')
        doctor_name = request.POST.get('doctor_name')
        appointment_date = request.POST.get('appointment_date')
        time_slot = request.POST.get('time_slot')
        problem = request.POST.get('problem')
        # gender = request.POST.get('gender')
        # address = request.POST.get('address')
        
        data = Appointment( Patient_id =Patient_id, department = department, doctor_name=doctor_name, appointment_date=appointment_date, time_slot=time_slot, problem= problem)
        
        data.save()
       

    return render(request,'dashboard/appointments/appoint_all.html', {"messages":data})


# ALL INVOICES SECTION
def ALL_INVOICE(request):
    data = Invoice.objects.all()
    if request.method == "POST":
        
        Patient_id = request.POST.get('patient_id')
        patient_name = request.POST.get('patient_name')
        department = request.POST.get('department')
        doctor_name = request.POST.get('doctor_name')
        addmission_date = request.POST.get('addmission_date')
        discharge_date = request.POST.get('discharge_date')
        cost = request.POST.get('cost')
        advance = request.POST.get('advance')
        pending = request.POST.get('pending')
        
        data = Invoice( Patient_id =Patient_id, patient_name = patient_name, department = department, doctor_name=doctor_name, addmission_date=addmission_date, discharge_date=discharge_date, cost= cost, advance=advance, pending=pending )
        
        data.save()
       

    return render(request,'dashboard/payment/invoice_all.html', {"messages":data})

# ALL ROOM SECTION
def ALL_ROOM(request):
    data = Room.objects.all()
    if request.method == "POST":
        
        Patient_id = request.POST.get('patient_id')
        patient_name = request.POST.get('patient_name')
        department = request.POST.get('department')
        doctor_name = request.POST.get('doctor_name')
        admission_date = request.POST.get('admission_date')
        discharge = request.POST.get('discharge')
        room_no = request.POST.get('room_no')
        room_type = request.POST.get('room_type')
       
        data = Room( Patient_id =Patient_id, patient_name = patient_name, department = department, doctor_name=doctor_name, admission_date=admission_date, discharge=discharge,room_no= room_no, room_type=room_type )
        
        data.save()
       

    return render(request,'dashboard/room/room_all.html', {"messages":data})



# ABOUT ABOUT PATIENT
def ABOUT_PATIENT(request):
    data = Patients.objects.all()
    if request.method == "POST":
        
        patient_name = request.POST.get('patient_name')
        dr_name = request.POST.get('dr_name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        data = Patients(patient_Name = patient_name, dr_Name = dr_name, date_of_birth=dob,age=age, phone=phone, email= email, gender=gender, address=address)
        
        data.save()
       

    return render(request,'dashboard/patient/pat_details.html', {"messages":data})



