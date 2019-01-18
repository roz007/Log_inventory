from django.contrib import admin
from django.urls import path , include
from .views import login, register ,register_item ,register_variant

urlpatterns = [
    path('login', login),
    path('register',register),
    path('create_new_item',register_item),
    path('create_new_variant',register_variant)
]
