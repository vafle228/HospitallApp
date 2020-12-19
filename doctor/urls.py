from . import views
from django.urls import re_path

urlpatterns = [
	re_path(r"^(?P<identifier>[\w.@+-]+)", views.doctorPage),
]