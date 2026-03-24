from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from rest_framework import viewsets

from .models import *
from .forms import *
from .serializers import *

# dashboard
@login_required
def dashboard(request):

    context={
    'doctors':Doctor.objects.count(),
    'patients':Patient.objects.count(),
    'appointments':Appointment.objects.count()
    }

    return render(request,'dashboard.html',context)


# login
def login_view(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('/')

    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')


# doctors
@login_required
def doctors_page(request):

    search=request.GET.get('search')

    data=Doctor.objects.all()

    if search:
        data=data.filter(name__icontains=search)

    paginator=Paginator(data,5)
    page=request.GET.get('page')
    data=paginator.get_page(page)

    return render(request,'doctors.html',{'doctors':data})


@login_required
def doctor_add(request):
    form=DoctorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/doctors/')
    return render(request,'form.html',{'form':form})


@login_required
def doctor_edit(request,id):
    data=get_object_or_404(Doctor,id=id)
    form=DoctorForm(request.POST or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/doctors/')
    return render(request,'form.html',{'form':form})


@login_required
def doctor_delete(request,id):
    data=get_object_or_404(Doctor,id=id)
    data.delete()
    return redirect('/doctors/')


# patients
@login_required
def patients_page(request):

    search=request.GET.get('search')
    data=Patient.objects.all()

    if search:
        data=data.filter(name__icontains=search)

    paginator=Paginator(data,5)
    page=request.GET.get('page')
    data=paginator.get_page(page)

    return render(request,'patients.html',{'patients':data})


@login_required
def patient_add(request):
    form=PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/patients/')
    return render(request,'form.html',{'form':form})


@login_required
def patient_edit(request,id):
    data=get_object_or_404(Patient,id=id)
    form=PatientForm(request.POST or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/patients/')
    return render(request,'form.html',{'form':form})


@login_required
def patient_delete(request,id):
    data=get_object_or_404(Patient,id=id)
    data.delete()
    return redirect('/patients/')


# appointments
@login_required
def appointments_page(request):

    data=Appointment.objects.all()

    paginator=Paginator(data,5)
    page=request.GET.get('page')
    data=paginator.get_page(page)

    return render(request,'appointments.html',{'appointments':data})


@login_required
def appointment_add(request):
    form=AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/appointments/')
    return render(request,'form.html',{'form':form})


@login_required
def appointment_edit(request,id):
    data=get_object_or_404(Appointment,id=id)
    form=AppointmentForm(request.POST or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/appointments/')
    return render(request,'form.html',{'form':form})


@login_required
def appointment_delete(request,id):
    data=get_object_or_404(Appointment,id=id)
    data.delete()
    return redirect('/appointments/')


# API
class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer