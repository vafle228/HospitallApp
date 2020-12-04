from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

appeal = (
    ("Заболел и пришел в первый раз", "Заболел"),
    ("На повторный прием", "Прием"),
    ("На выписку", "Выписка")
)

professions = (
    ("Офтальмолог", "Офтальмолог"),
    ("Хирург", "Хирург"),
    ("Психиатр", "Психиатр"),
    ("Оттолоринголог", "Оттолоринголог"),
    ("Стоматолог", "Стоматолог"),
    ("Невролог", "Невролог"),
    ("Педиатр", "Педиатр"),
    ("Кардиолог", "Кардиолог"),
)


class HospitalUser(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=60, choices=(("Мужской", "М"), ("Женский", "Ж")))
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Doctor(models.Model):
    doctor_name = models.ForeignKey(HospitalUser, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100, choices=professions, default="врач")
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.doctor_name.name}'


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=None)
    client_name = models.ForeignKey(HospitalUser, on_delete=models.CASCADE)
    appointment_time = models.TimeField(default=timezone.now)
    appointment_date = models.DateField(default=datetime.now)
    client_appeal = models.CharField(max_length=60, choices=appeal, default="Заболел")

    def __str__(self):
        return f'{self.client_name.name} appointment'
