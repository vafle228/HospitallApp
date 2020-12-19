from django import forms
from login.models import Doctor, HospitalUser, Appointment


class AppointmentForm(forms.Form):
    specialist = forms.CharField(required=True)
    date = forms.DateField(required=True)
    time = forms.TimeField(required=True)
    appeal = forms.CharField(required=True)
    endTime = forms.TimeField(required=True)

    def save(self, user):
        specialist = self.cleaned_data['specialist']
        appeal = self.cleaned_data['appeal']
        date = self.cleaned_data['date']
        time = self.cleaned_data['time']
        endTime = self.cleaned_data['endTime']

        appointment = Appointment.objects.create(
            doctor=Doctor.objects.filter(pk=int(specialist))[0],
            client_name=HospitalUser.objects.filter(name=user)[0],
            appointment_start=time,
            appointment_end=endTime,
            appointment_date=date,
            client_appeal=appeal
        )
        appointment.save()
        return True
