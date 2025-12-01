"""
конфигурация asgi для проекта med_reviews.

он предоставляет asgi callable как переменную уровня модуля с именем ``application``.

для получения дополнительной информации об этом файле см.
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'med_reviews.settings')

application = get_asgi_application()
