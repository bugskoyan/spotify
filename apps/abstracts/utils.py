# Python
from typing import Any

# Django
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import Http404


def send_email(
    subject: str,
    body: str,
    to_emails: list[str]
) -> None:
    email = EmailMessage(
        subject,
        body,
        settings.EMAIL_FROM,
        to_emails
    )
    email.send()


def normalize_time(duration: int) -> str:
    SECONDS_PER_MINUTE: int = 60
    minutes, seconds = divmod(
        duration,
        SECONDS_PER_MINUTE
    )
    return f'{int(minutes)} мин {int(seconds)} сек'


def get_object_or_404(
    model: Any,
    object_id: int
) -> Any:
    try:
        return model.objects.get(
            id=object_id
        )
    except model.DoesNotExist:
        raise Http404
