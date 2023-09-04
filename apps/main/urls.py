# Django
from django.urls import path

# Local
from .views import (
    DetailView,
    IndexView,
    create_song,
    DeleteView,
    favorite
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:album_id>/', DetailView.as_view(), name='detail'),
    path('<int:album_id>/create_song/', create_song, name='create_song'),
    path('<int:song_id>/favorite/', favorite, name='favorite'),
    path(
        '<int:album_id>/delete_song/<int:song_id>/',
        DeleteView.as_view(),
        name='delete_song'
    ),
]