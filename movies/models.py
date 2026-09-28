from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    class Status(models.TextChoices):
        WANT_TO_WATCH = "want", "Baxmaq istəyirəm"
        WATCHING = "watching", "Baxıram"
        WATCHED = "watched", "Baxmışam"

    title = models.CharField("Filmin adı", max_length=200)
    genre = models.CharField("Janr", max_length=80)
    release_year = models.PositiveSmallIntegerField("Buraxılış ili", validators=[MinValueValidator(1888)])
    status = models.CharField("Status", max_length=12, choices=Status.choices, default=Status.WANT_TO_WATCH)
    rating = models.PositiveSmallIntegerField(
        "Şəxsi qiymətləndirmə", null=True, blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="İstəyə bağlıdır; 1–10 arası qiymət daxil edin.",
    )
    created_at = models.DateTimeField("Əlavə olunma tarixi", auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movies", verbose_name="Filmin sahibi")

    class Meta:
        ordering = ["-created_at", "title"]
        verbose_name = "Film"
        verbose_name_plural = "Filmlər"

    def __str__(self):
        return f"{self.title} ({self.release_year})"
