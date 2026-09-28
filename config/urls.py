from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("movies.api_urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("movies.auth_urls")),
    path("", RedirectView.as_view(pattern_name="movie-list", permanent=False)),
    path("", include("movies.urls")),
]
