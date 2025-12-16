from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/doctors/', views.api_doctors, name='api_doctors'),
]

