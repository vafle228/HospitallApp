from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from login.models import Appointment, HospitalUser, Doctor


def doctorPage(request, identifier):
    if User.objects.filter(pk=identifier).exists():
        user = User.objects.filter(pk=identifier)[0]
        if request.user == user and request.user.is_authenticated:
            hospital_user = HospitalUser.objects.filter(name=user)[0]
            if Doctor.objects.filter(doctor_name=hospital_user).exists():
                doctor = Doctor.objects.filter(doctor_name=hospital_user)[0]
                appointments = Appointment.objects.filter(doctor=doctor,
                                                          appointment_date=datetime.today())

                return render(request, 'doctor/index.html', {'appointments': appointments[1::],
                                                             'current_appointment': appointments[0],
                                                             'id': identifier})
    return redirect('/login/doctor')
