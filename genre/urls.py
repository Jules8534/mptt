from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="homepage"),
    path("addfile/", views.add_file, name="yougotitfiles"),
]