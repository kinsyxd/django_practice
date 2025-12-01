"""
конфигурация wsgi для проекта med_reviews.

он предоставляет wsgi callable как переменную уровня модуля с именем ``application``.

для получения дополнительной информации об этом файле см.
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'med_reviews.settings')

application = get_wsgi_application()
