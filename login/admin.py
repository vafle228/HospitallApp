from django.contrib import admin
from .models import HospitalUser, Doctor, Appointment

admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(HospitalUser)
