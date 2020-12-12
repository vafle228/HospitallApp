from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import HospitalUser
from django.contrib.auth.password_validation import validate_password


class LoginUser(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    def save(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if User.objects.filter(email=email).exists():
            user = authenticate(username=User.objects.filter(email=email)[0].username, password=password)
            if (user is not None) and user.is_active:
                return user
        return 'Error'


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    name = forms.CharField(required=True)

    def save(self):
        email = self.cleaned_data['email']
        name = self.cleaned_data['name']
        password = self.cleaned_data['password']

        if not User.objects.filter(email=email).exists():
            try:
                validate_password(password)
            except forms.ValidationError:
                return 'Error'

            user = User.objects.create_user(name, email, password)
            user.save()

            hospital_user = HospitalUser.objects.create(name=user, gender="M", age=25)
            hospital_user.save()

            return user
        return 'Error'
