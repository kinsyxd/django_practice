# МедОтзывы

Учебный набросок сервиса отзывов о врачах на Django + Vite.

## Структура проекта

```
django_practice/
  med_reviews/     - настройки Django
  doctors/         - приложение отзовика
    views.py       - логика проброса данных
    urls.py        - маршрутизация
    templates/     - HTML-шаблоны
  frontend/        - исходники фронтенда (CSS/JS)
  static/          - статические файлы
  vite.config.js   - конфигурация Vite
```

## Компоненты системы

### 1. Проброс данных (doctors/views.py)

Функция index() формирует словарь context и передает его в шаблон через render().

Структура context:
- page_title - заголовок страницы
- specialties - список специальностей (name)
- doctors - список врачей (name, specialty, clinic, rating, review, reviewer)

### 2. Маршрутизация (doctors/urls.py)

Связывает корневой URL с функцией index.

### 3. Шаблон (doctors/templates/doctors/index.html)

HTML-файл с Django-тегами:
- {{ variable }} - вывод переменных из context
- {% for item in list %} - итерация по спискам

### 4. Фронтенд (frontend/)

Vite собирает CSS/JS и отдает их Django-шаблону.
Включен хот релоад.

## Запуск
Сначала запускаем Vite:
```
npm run dev
```

Затем - Django:
```
venv\Scripts\activate
python manage.py runserver
```

Ссылка на стенд: http://127.0.0.1:8000/