from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm


def loginUserPage(request):
    return render(request, 'login/user.html')


def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.save()

            if user != 'Error':
                login(request, user)
                return redirect(f'/user/{user.pk}')
    return redirect('/login/user')


def registerUser(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm-pass']:
            form = RegisterForm({'email': request.POST['email'],
                                 'password': request.POST['password'],
                                 'name': request.POST['name']})
            if form.is_valid():
                user = form.save()
                if user != 'Error':
                    login(request, user)
                    return redirect(f'/user/{user.pk}')
    return redirect('/login/user')


def loginDoctorPage(request):
    return render(request, 'login/doctor.html')


def loginDoctor(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.save()

            if user != 'Error':
                login(request, user)
                return redirect(f'/doctor/{user.pk}')
    return redirect('/login/doctor')
