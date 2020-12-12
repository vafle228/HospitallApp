from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import LoginUser, RegisterForm


def loginPage(request):
    return render(request, 'login/index.html')


def loginUser(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)

        if form.is_valid():
            user = form.save()

            if user != 'Error':
                login(request, user)
                return redirect(f'/main/{user.pk}')
    return redirect('/login/')


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
                    return redirect(f'/main/{user.pk}')
    return redirect('/login/')
