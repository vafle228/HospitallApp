from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.loginUserPage),
    path('doctor/', views.loginDoctorPage),
    path('login_user/', views.loginUser, name='login-user'),
    path('login_doctor/', views.loginDoctor, name='login-doctor'),
    path('register_user/', views.registerUser, name='register-user')
]
