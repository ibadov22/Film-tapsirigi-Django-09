from rest_framework import viewsets

from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        # Every API action, including detail/update/delete, is scoped to the caller.
        queryset = Movie.objects.filter(owner=self.request.user)
        status = self.request.query_params.get("status")
        genre = self.request.query_params.get("genre")

        if status in Movie.Status.values:
            queryset = queryset.filter(status=status)
        if genre:
            queryset = queryset.filter(genre__iexact=genre.strip())
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
