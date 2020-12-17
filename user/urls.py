from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^appointment_check/(?P<identifier>[\w.@+-]+)", views.appointmentCheck),
    re_path(r"^appointment_create/(?P<identifier>[\w.@+-]+)", views.appointmentCreate),
    re_path(r"^appointment_delete/(?P<identifier>[\w.@+-]+)", views.appointmentRemove),
    re_path(r"^appointment_logout/(?P<identifier>[\w.@+-]+)", views.logoutUser),
    re_path(r"^(?P<identifier>[\w.@+-]+)", views.userPage),
]
