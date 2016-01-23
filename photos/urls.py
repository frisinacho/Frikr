from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from photos.api import PhotoViewSet
from photos.views import HomeView, DetailView, CreateView, PhotoListView, UserPhotosView
from rest_framework.routers import DefaultRouter


# APIRouter
router = DefaultRouter()
router.register(r'api/1.0/photos', PhotoViewSet)


urlpatterns = [
    # Photos URLs
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'^my-photos/$', login_required(UserPhotosView.as_view()), name='user_photos'),
    url(r'^photos/$', PhotoListView.as_view(), name='photos_list'),
    url(r'^photos/(?P<pk>[0-9]+)$', DetailView.as_view(), name='photo_detail'),
    url(r'photos/new$', CreateView.as_view(), name='create_photo'),

    # API URLs
    url(r'', include(router.urls)),   # Incluyo las URLs de API
]
