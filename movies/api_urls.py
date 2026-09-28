from rest_framework.routers import DefaultRouter

from .api import MovieViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="api-movie")

urlpatterns = router.urls
