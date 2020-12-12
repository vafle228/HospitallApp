from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from login.models import Appointment, HospitalUser, Doctor
from .insertClient import insertClient
from .forms import AppointmentForm


def userPage(request, identifier):
    if User.objects.filter(pk=identifier).exists():
        user = User.objects.filter(pk=identifier)[0]
        if request.user == user and request.user.is_authenticated:
            hospital_user = HospitalUser.objects.filter(name=user)[0]
            appointments = Appointment.objects.filter(client_name=hospital_user)

            return render(request, 'user/index.html', {'appointments': appointments, 'id': identifier})
    return redirect('/login/')


def appointmentCheck(request, identifier):
    if User.objects.filter(pk=identifier).exists():
        user = User.objects.filter(pk=identifier)[0]

        if request.method == "POST" and request.user == user and request.user.is_authenticated:
            form = AppointmentForm(request.POST)
            if form.is_valid():
                variants, client_referral = [], createReferral(request.user, form.cleaned_data['date'])
                time, date = ':'.join(str(form.cleaned_data['time']).split(':')[:2]), form.cleaned_data['date']

                for doctor in Doctor.objects.filter(profession=form.cleaned_data['specialist']):
                    variant = insertClient(time, 600, createQue(doctor, date), client_referral, date, doctor)
                    if isinstance(variant, dict):
                        return JsonResponse([True, variant], safe=False)
                    variants += variant
                return JsonResponse([False, variants], safe=False)
    return HttpResponse("Error")


def appointmentCreate(request, identifier):
    if User.objects.filter(pk=identifier).exists():
        user = User.objects.filter(pk=identifier)[0]
        if request.method == "POST" and request.user == user and request.user.is_authenticated:
            data = {'specialist': Doctor.objects.filter(pk=request.POST['specialist'])}
            form = AppointmentForm(request.POST)
            if form.is_valid():
                # form.save(variant, HospitalUser.objects.filter(name=user))
                return redirect(f'/main/{request.user.pk}')
        return redirect(f'/main/{request.user.pk}')


def createQue(doctor, date):
    appointments, que = Appointment.objects.filter(doctor=doctor, appointment_date=date), []
    for appointment in appointments:
        que.append({'time': ':'.join(str(appointment.appointment_start).split(':')[:2]),
                    'endTime': ':'.join(str(appointment.appointment_end).split(':')[:2]),
                    'doctor': doctor,
                    'date': date})
    return que


def createReferral(user, date):
    hospital_user = HospitalUser.objects.filter(name=user)[0]
    appointments = Appointment.objects.filter(client_name=hospital_user, appointment_date=date)
    referral = []

    for appointment in appointments:
        referral.append({'time': ':'.join(str(appointment.appointment_start).split(':')[:2]),
                         'endTime': ':'.join(str(appointment.appointment_end).split(':')[:2]),
                         'doctor': appointment.doctor,
                         'date': appointment.appointment_date})
    return referral
