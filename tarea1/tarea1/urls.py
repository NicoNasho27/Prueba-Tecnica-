from django.contrib import admin
from django.urls import path
from request.views import post

urlpatterns = [
    path('', post),
]
