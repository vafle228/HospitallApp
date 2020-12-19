from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from login.models import Appointment, HospitalUser, Doctor
from .insertClient import insertClient
from .forms import AppointmentForm
from datetime import datetime
from django.contrib.auth import logout

doctors = ["Офтальмолог", "Хирург", "Психиатр", "Оттолоринголог", "Стоматолог", "Невролог", "Педиатр", "Кардиолог"]
reason = ["Выписка", "Прием", "Заболел"]


def logoutUser(request, identifier):
    logout(request)
    return redirect('/login/user')


def userPage(request, identifier):
    if User.objects.filter(pk=identifier).exists():
        user = User.objects.filter(pk=identifier)[0]
        if request.user == user and request.user.is_authenticated:
            hospital_user = HospitalUser.objects.filter(name=user)[0]
            appointments = Appointment.objects.filter(client_name=hospital_user,
                                                      appointment_date__gte=datetime.today())

            return render(request, 'user/index.html', {'appointments': appointments, 'id': identifier})
    return redirect('/login/user')


def appointmentCheck(request, identifier):
    if User.objects.filter(pk=identifier).exists():
        user, variants = User.objects.filter(pk=identifier)[0], {}

        if request.method == "POST" and request.user == user and request.user.is_authenticated:
            specialist = request.POST['specialist']
            appeal = request.POST['appeal']
            date = request.POST['date']

            if specialist not in doctors or appeal not in reason:
                return HttpResponse('Error')

            for doctor in Doctor.objects.filter(profession=specialist):
                doctor_name = doctor.doctor_name.name.username
                que, client_referral = createQue(doctor, date), createReferral(user, date)
                variants[doctor_name] = insertClient(600, que, client_referral, date, doctor)
            return JsonResponse(variants)
    return HttpResponse('Error')


def appointmentCreate(request, identifier):
    if User.objects.filter(pk=identifier).exists():
        user = User.objects.filter(pk=identifier)[0]
        if request.method == "POST" and request.user == user and request.user.is_authenticated:
            form = AppointmentForm(request.POST)
            if form.is_valid():
                form.save(user)
            return HttpResponse(f'/user/{user.pk}')
    return HttpResponse('/login/user')


def appointmentRemove(request, identifier):
    if User.objects.filter(pk=identifier).exists():
        user = User.objects.filter(pk=identifier)[0]
        if request.method == "POST" and request.user == user and request.user.is_authenticated:
            if Appointment.objects.filter().exists():
                Appointment.objects.filter(pk=request.POST['appointment']).delete()
            return HttpResponse(f'/user/{user.pk}')
    return HttpResponse('/login/user')


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
