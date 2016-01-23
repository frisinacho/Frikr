from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from users.api import UserViewSet


# APIRouter
router = DefaultRouter()
router.register(r'api/1.0/users', UserViewSet, base_name='user')


urlpatterns = [
    # API URLs
    url(r'', include(router.urls)),   # Incluyo las URLs de API
]
