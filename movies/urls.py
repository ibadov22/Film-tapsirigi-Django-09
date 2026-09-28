from django.urls import path
from .views import MovieCreateView, MovieDeleteView, MovieListView, MovieUpdateView

urlpatterns = [
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/add/", MovieCreateView.as_view(), name="movie-add"),
    path("movies/<int:pk>/edit/", MovieUpdateView.as_view(), name="movie-edit"),
    path("movies/<int:pk>/delete/", MovieDeleteView.as_view(), name="movie-delete"),
]
