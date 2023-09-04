# Python
from typing import Optional

# Django
from django.contrib import admin

# Local
from .models import (
    Album,
    Artist,
    Band,
    Country,
    Genre,
    Song
)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """
    CountryAdmin admin.
    """
    readonly_fields = ()


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    """
    BandAdmin admin.
    """
    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted'
    )


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    readonly_fields: tuple[str, ...] = (
        'gender',
    )

    def get_readonly_fields(
        self,
        request,
        obj: Optional[Artist] = None
    ) -> tuple[str, ...]:
        if obj is None:
            return ()

        return self.readonly_fields


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields: tuple[str, ...] = (
        'status',
    )

    def get_readonly_fields(
        self,
        request,
        obj: Optional[Artist] = None
    ) -> tuple[str, ...]:
        if obj is None:
            return self.readonly_fields

        return self.readonly_fields + ('release_date',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    readonly_fields: tuple[str, ...] = (
        'duration',
        'times_played'
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
