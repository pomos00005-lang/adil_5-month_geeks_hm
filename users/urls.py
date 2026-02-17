from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('registration/',views.registration_api_view),
    path('auth/',views.autherithezion_api_view),
]
