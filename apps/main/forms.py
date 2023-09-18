# Django
from django import forms
from django.core.exceptions import ValidationError

from typing import Any, Dict

# Local
from .models import (
    Album,
    Song
)


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['band', 'title', 'logo']


class SongForm(forms.ModelForm):




    class Meta:
        model = Song
        fields = ['title', 'audio_file']