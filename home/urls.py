from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('<id>/delete/', views.delete_catatan),

]