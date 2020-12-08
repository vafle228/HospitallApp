from datetime import datetime
from time import strptime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from login.models import Appointment, HospitalUser, Doctor
from .insertClient import insertClient


def userPage(request, username):
    user = User.objects.filter(username=username)[0]
    if request.user == user:
        hospital_user = HospitalUser.objects.filter(name=user)[0]
        appointments = Appointment.objects.filter(client_name=hospital_user)

        if request.method == 'POST':
            specialist = request.POST['specialist']
            date = request.POST['date']
            time = request.POST['time']

            if not(validTime(time)) or not(validDate(date)):
                return render(request, 'user/index.html', {'appointments': appointments})

            variants = insertClient(user, time, 600, specialist, Doctor, Appointment, HospitalUser)
            print(variants)

            appointment = Appointment.objects.create(
                doctor=Doctor.objects.filter(profession=specialist)[0],
                client_name=hospital_user,
                appointment_start=variants[0]['time'],
                appointment_end=variants[0]['endTime'],
                appointment_date=date,
                client_appeal='Заболел'
            )
            appointment.save()
            return redirect(f'/main/{username}')

        return render(request, 'user/index.html', {'appointments': appointments})
    return redirect('/login/')


def validDate(date):
    date = list(map(int, date.split('-')))
    day, month, year = date[2], date[1], date[0]
    datetime(year, month, day)
    try:
        datetime(year, month, day)
    except ValueError:
        return False
    return True


def validTime(time):
    try:
        strptime(time, '%H:%M')
    except ValueError:
        return False
    return True

