from django.conf.urls import include, url
from photos.api import PhotoViewSet
from rest_framework.routers import DefaultRouter


# APIRouter
router = DefaultRouter()
router.register(r'api/1.0/photos', PhotoViewSet)


urlpatterns = [
    # API URLs
    url(r'', include(router.urls)),   # Incluyo las URLs de API
]
