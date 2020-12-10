from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import LoginUser


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
