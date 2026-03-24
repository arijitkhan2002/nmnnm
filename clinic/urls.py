from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('doctors-api',DoctorViewSet)
router.register('patients-api',PatientViewSet)
router.register('appointments-api',AppointmentViewSet)

urlpatterns=[

path('',dashboard),

path('login/',login_view),
path('logout/',logout_view),

path('doctors/',doctors_page),
path('doctor-add/',doctor_add),
path('doctor-edit/<int:id>/',doctor_edit),
path('doctor-delete/<int:id>/',doctor_delete),

path('patients/',patients_page),
path('patient-add/',patient_add),
path('patient-edit/<int:id>/',patient_edit),
path('patient-delete/<int:id>/',patient_delete),

path('appointments/',appointments_page),
path('appointment-add/',appointment_add),
path('appointment-edit/<int:id>/',appointment_edit),
path('appointment-delete/<int:id>/',appointment_delete),

path('api/',include(router.urls)),
]