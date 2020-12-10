from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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
