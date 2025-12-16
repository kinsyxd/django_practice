from django.shortcuts import render
from django.http import JsonResponse
from .models import Doctor


def index(request):
    """главная страница с базовым контекстом"""
    context = {
        'page_title': 'Лучшие врачи вашего города',
        'specialties': [
            {'name': 'Терапевты'},
            {'name': 'Кардиологи'},
            {'name': 'Стоматологи'},
        ],
    }
    return render(request, 'doctors/index.html', context)


def api_doctors(request):
    """API-эндпоинт: возвращает список врачей из БД в формате JSON."""
    doctors = Doctor.objects.all()
    doctors_list = [
        {
            'id': doctor.id,
            'name': doctor.name,
            'specialty': doctor.specialty,
            'clinic': doctor.clinic,
            'rating': doctor.rating,
            'review': doctor.review,
            'reviewer': doctor.reviewer,
        }
        for doctor in doctors
    ]
    return JsonResponse({'doctors': doctors_list})
