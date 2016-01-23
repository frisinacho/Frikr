from django.conf.urls import include, url
from photos.api import PhotoViewSet
from rest_framework.routers import DefaultRouter


# APIRouter
router = DefaultRouter()
router.register(r'photos', PhotoViewSet)


urlpatterns = [
    # API URLs
    url(r'1.0/', include(router.urls)),   # Incluyo las URLs de API
]
