
from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.Index, name='dashboard'),
    # path("base", views.Base, name="base"),
    path('Patient/Add',views.ADD_PATIENT,name='add_patient'),
    path('doctor/Add',views.ADD_DOCTOR,name='add_doctor'),
    path('Appointment/Add',views.ADD_APPOINTMENT,name='add_appointment'),
    path('Invoice/Add',views.ADD_INVOICE,name='add_invoice'),
    
    path('Patient/All',views.ALL_PATIENT,name='patients_all'),
    path('Doctor/All',views.ALL_DOCTOR,name='doctor_all'),
    path('Appointment/All',views.ALL_APPOINTMENT,name='appointment_all'),
    path('Invoice/All',views.ALL_INVOICE,name='invoice_all'),
    path('Patient/About',views.ABOUT_PATIENT,name='patients_about'),
    # path('Doctor/About',views.ABOUT_DOCTOR,name='doctor_about'),
   
]
