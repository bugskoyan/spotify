# Django
from django.db import models


class AbsctractDateTime(models.Model):
    """
    AbsctractDateTime model.
    """
    datetime_created = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    datetime_updated = models.DateTimeField(
        verbose_name='дата обновления',
        auto_now=True
    )
    datetime_deleted = models.DateTimeField(
        verbose_name='дата удаления',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
