from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'Лучшие врачи вашего города',
        'specialties': [
            {'name': 'Терапевты'},
            {'name': 'Кардиологи'},
            {'name': 'Стоматологи'},
        ],
        'doctors': [
            {
                'name': 'Иванов Петр Сергеевич',
                'specialty': 'Хирург',
                'clinic': 'ГКБ №1',
                'rating': 5,
                'review': 'Отличный специалист! Провел операцию на высшем уровне.',
                'reviewer': 'Анна М.',
            },
            {
                'name': 'Петрова Мария Александровна',
                'specialty': 'Кардиолог',
                'clinic': 'Кардиоцентр "Здоровье"',
                'rating': 4,
                'review': 'Грамотный врач, помогла разобраться с проблемами сердца.',
                'reviewer': 'Сергей К.',
            },
            {
                'name': 'Сидоров Алексей Николаевич',
                'specialty': 'Стоматолог',
                'clinic': 'Стоматология "Улыбка"',
                'rating': 5,
                'review': 'Лечил зубы безболезненно, современное оборудование.',
                'reviewer': 'Елена В.',
            },
        ],
    }
    return render(request, 'doctors/index.html', context)
