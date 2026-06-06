from django.urls import path
from .import views

urlpatterns = [
    path('get_register/',views.get_register),
    path('',views.fuel_calculator),
]