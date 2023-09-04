# Python
from typing import Any

# Django
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args: Any, **kwargs: Any) -> None:
        try:
            User.objects.create_superuser(
                username='root2',
                email='root2@mail.cc',
                password='bc83cg378cg3c',
                first_name='Иван',
                last_name='Темнохолмов'
            )
            print('Админ успешно создан')
        except Exception as exc:
            print(f'Админ не создан: {str(exc)}')
