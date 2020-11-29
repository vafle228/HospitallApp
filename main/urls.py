from django.urls import path
from .views import mainPage

urlpatterns = [
    path('main/', mainPage)
]
