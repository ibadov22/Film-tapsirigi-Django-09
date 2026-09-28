from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    status_display = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "genre",
            "release_year",
            "status",
            "status_display",
            "rating",
            "created_at",
            "owner",
        ]
        read_only_fields = ["id", "created_at", "owner"]
