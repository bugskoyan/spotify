# Python
from typing import Any

# Django
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

# First party
from abstracts.utils import get_object_or_404

# Local
from .models import (
    Album,
    Artist,
    Song,
    AudioFileType
)

from .forms import SongForm, AlbumForm


#-------------------------------------------------
# Example of Function Based View (FBV)
#
# def index(request: WSGIRequest) -> HttpResponse:
#     albums: QuerySet[Album] = Album.objects.all()
#     context: dict[str, QuerySet[Any]] = {
#         'albums': albums
#     }
#     return render(
#         request,
#         'main/index.html',
#         context
#     )


    

class IndexView(View):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, QuerySet[Any]]:
        albums: QuerySet[Album] = Album.objects.all()
        context: dict[str, QuerySet[Any]] = {
            'albums': albums
        }
        return context

    def get(
        self,
        request: WSGIRequest,
        *args: Any,
        **kwargs: Any
    ) -> HttpResponse:
        context: dict[str, QuerySet[Any]] = self.get_context_data()
        return render(
            request,
            self.template_name,
            context
        )


class DetailView(View):
    template_name = 'main/detail.html'

    def get_context_data(
        self,
        album_id: int,
        **kwargs: Any
    ) -> dict[str, QuerySet[Any]]:
        album: Album = get_object_or_404(
            Album,
            album_id
        )
        user: User = self.request.user
        context: dict[str, QuerySet[Any]] = {
            'album': album,
            'user': user
        }
        return context

    def get(
        self,
        request: WSGIRequest,
        album_id: int,
        *args: Any,
        **kwargs: Any
    ) -> HttpResponse:
        context: dict[str, QuerySet[Any]] = self.get_context_data(
            album_id
        )
        return render(
            request,
            self.template_name,
            context
        )


def favorite(
    request: WSGIRequest,
    song_id: int
) -> JsonResponse:
    song: Song = get_object_or_404(
        Song,
        song_id
    )
    try:
        song.is_favorite = True if song.is_favorite is False else False
        song.save(update_fields=('is_favorite',))
    except (
        KeyError,
        Song.DoesNotExist
    ):
        return JsonResponse({'success': False})
    return JsonResponse({'success': True})


class DeleteView(View):
    template_name = 'main/detail.html'

    def get_context_data(
        self,
        album_id: int,
        **kwargs: Any
    ) -> dict[str, QuerySet[Any]]:
        album: Album = get_object_or_404(
            Album,
            album_id
        )
        context: dict[str, QuerySet[Any]] = {
            'album': album
        }
        return context

    def post(
        self,
        request: WSGIRequest,
        album_id: int,
        song_id: int,
        *args: Any,
        **kwargs: Any
    ) -> HttpResponse:
        context: dict[str, QuerySet[Any]] = self.get_context_data(
            album_id
        )
        song: Song = context['album'].song_set.get(
            id=song_id
        )
        song.delete()

        return render(
            request,
            self.template_name,
            context
        )






class CreateSongView(View):
    """
    Вьюшка для создания песен.
    """
    def get(
        self,
        request: WSGIRequest,
        album_id: int
    ) -> HttpResponse:

        album: Album = get_object_or_404(
            Album,
            album_id
        )
        form: SongForm = SongForm()
        context: dict[str, Any] = {
            'album': album,
            'form': form
        }
        return render(
            request,
            'main/create_song.html',
            context
        )

    def post(
        self,
        request: WSGIRequest,
        album_id: int
    ) -> HttpResponse:

        album: Album = get_object_or_404(
            Album,
            album_id
        )
        form: SongForm = SongForm(
            request.POST or None,
            request.FILES or None
        )
        if not form.is_valid():
            return render(
                request,
                'main/create_song.html',
                {
                    'album': album,
                    'form': form
                }
            )

        album_songs: QuerySet[Song] = album.songs.all()
        for song in album_songs:
            if song.title == form.cleaned_data.get('title'):
                return render(
                    request,
                    'main/create_song.html',
                    {
                        'album': album,
                        'form': form,
                        'error_message': 'Вы уже добавляли эту песню'
                    }
                )

        song: SongForm = form.save(commit=False)
        song.album = album
        song.audio_file = request.FILES['audio_file']

        file_type: str = song.audio_file.url.split('.')[-1]
        file_type = file_type.lower()

        audio_file_types: QuerySet[str] = \
            AudioFileType.objects.values_list(
                'name',
                flat=True
            )

        if file_type not in audio_file_types:
            return render(
                request,
                'main/create_song.html',
                {
                    'album': album,
                    'form': form,
                    'error_message': 'Неверный формат аудио-файла'
                }
            )

        song.save()
        return render(
            request,
            'main/detail.html',
            {
                'album': album}
            )
