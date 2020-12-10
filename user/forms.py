from django import forms
from login.models import Appointment

doctors = ["Офтальмолог", "Хирург", "Психиатр", "Оттолоринголог", "Стоматолог", "Невролог", "Педиатр", "Кардиолог"]
reason = ["Заболел и пришел в первый раз", "На повторный прием", "На выписку"]


class AppointmentForm(forms.Form):
    specialist = forms.CharField(required=True)
    date = forms.DateField(required=True)
    time = forms.TimeField(required=True)
    appeal = forms.CharField(required=True)

    def save(self, variant, user):
        specialist = self.cleaned_data['specialist']
        appeal = self.cleaned_data['appeal']
        date = self.cleaned_data['date']

        if specialist not in doctors or appeal not in reason:
            return 'Error'

        appointment = Appointment.objects.create(
            doctor=variant['doctor'],
            client_name=user,
            appointment_start=variant['time'],
            appointment_end=variant['endTime'],
            appointment_date=date,
            client_appeal=appeal
        )
        appointment.save()
        return True
