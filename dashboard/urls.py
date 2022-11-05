
from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.index, name="dashboard"),
    path("base", views.Base, name="base"),
    path('Patient/Add',views.ADD_PATIENT,name='add_patient'),
    path('Patient/All',views.ALL_PATIENT,name='patients_all'),
   
]
