from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import MovieForm
from .models import Movie


class MovieListView(LoginRequiredMixin, ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    context_object_name = "movies"
    paginate_by = 10

    def get_queryset(self):
        # Start with the current user's rows, before applying any user-controlled filters.
        queryset = Movie.objects.filter(owner=self.request.user)
        status = self.request.GET.get("status", "")
        genre = self.request.GET.get("genre", "")
        if status in Movie.Status.values:
            queryset = queryset.filter(status=status)
        if genre:
            queryset = queryset.filter(genre__iexact=genre)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Movie.objects.filter(owner=self.request.user).order_by("genre").values_list("genre", flat=True).distinct()
        context["status_choices"] = Movie.Status.choices
        context["selected_status"] = self.request.GET.get("status", "")
        context["selected_genre"] = self.request.GET.get("genre", "")
        return context


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = "movies/movie_form.html"
    success_url = reverse_lazy("movie-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Film siyahınıza əlavə edildi.")
        return super().form_valid(form)


class OwnedMovieMixin(LoginRequiredMixin):
    model = Movie
    # Returning 404 for another user's object avoids disclosing its existence.
    def get_queryset(self):
        return Movie.objects.filter(owner=self.request.user)


class MovieUpdateView(OwnedMovieMixin, UpdateView):
    form_class = MovieForm
    template_name = "movies/movie_form.html"
    success_url = reverse_lazy("movie-list")

    def form_valid(self, form):
        messages.success(self.request, "Film məlumatları yeniləndi.")
        return super().form_valid(form)


class MovieDeleteView(OwnedMovieMixin, DeleteView):
    template_name = "movies/movie_confirm_delete.html"
    success_url = reverse_lazy("movie-list")

    def form_valid(self, form):
        messages.success(self.request, "Film siyahınızdan silindi.")
        return super().form_valid(form)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("movie-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
