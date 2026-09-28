from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "genre", "release_year", "status", "rating"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Məsələn, Interstellar"}),
            "genre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Məsələn, Elmi fantastika"}),
            "release_year": forms.NumberInput(attrs={"class": "form-control", "placeholder": "2014", "min": 1888}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "placeholder": "1–10", "min": 1, "max": 10}),
        }
