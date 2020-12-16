from django.urls import re_path
from .views import appointmentCheck, userPage, appointmentCreate

urlpatterns = [
    re_path(r"^appointment_check/(?P<identifier>[\w.@+-]+)", appointmentCheck),
    re_path(r"^appointment_create/(?P<identifier>[\w.@+-]+)", appointmentCreate),
    re_path(r"^(?P<identifier>[\w.@+-]+)", userPage),
]
