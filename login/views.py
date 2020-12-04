from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def loginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(email=email)

        if len(user):
            if check_password(password, user[0].password):
                login(request, user[0])
                return redirect(f'/main/{user[0].username}')

    return render(request, 'login/index.html')
