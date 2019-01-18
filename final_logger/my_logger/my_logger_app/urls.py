from django.contrib import admin
from django.urls import path , include
from .views import login, register

urlpatterns = [
    path('login', login),
    path('register',register)
]
