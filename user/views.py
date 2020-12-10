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
                variants, client_referral = [], createReferral(request.user)
                time = ':'.join(str(form.cleaned_data['time']).split(':')[:2])

                for doctor in Doctor.objects.filter(profession=form.cleaned_data['specialist']):
                    variant = insertClient(time, 600, createQue(doctor), client_referral)
                    if isinstance(variant, dict):
                        return HttpResponse(None)
                    variants += variant
                print(type(variants[0]))
                return JsonResponse(variants, safe=False)
    return HttpResponse("Error")


def appointmentCreate(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            variants, client_referral, time = [], createReferral(request.user), form.cleaned_data['time']
            for doctor in Doctor.objects.filter(profession=form.cleaned_data['specialist']):
                variant = insertClient(time, 600, createQue(doctor), client_referral)
                if isinstance(variant, dict):
                    form.save(variant, HospitalUser.objects.filter(name=request.user))
                    return redirect(f'/main/{request.user.username}')
                variants.append(variant)
        return redirect(f'/main/{request.user.username}')


def createQue(doctor):
    appointments, que = Appointment.objects.filter(doctor=doctor), []
    for appointment in appointments:
        que.append({'time': ':'.join(str(appointment.appointment_start).split(':')[:2]),
                    'endTime': ':'.join(str(appointment.appointment_end).split(':')[:2]),
                    'doctor': doctor
                    })
    return que


def createReferral(user):
    hospital_user = HospitalUser.objects.filter(name=user)[0]
    appointments = Appointment.objects.filter(client_name=hospital_user)
    referral = []

    for appointment in appointments:
        referral.append({'time': ':'.join(str(appointment.appointment_start).split(':')[:2]),
                         'endTime': ':'.join(str(appointment.appointment_end).split(':')[:2]),
                         'doctor': appointment.doctor
                         })
    return referral
