from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from photos.views import HomeView, DetailView, CreateView, PhotoListView, UserPhotosView


urlpatterns = [
    # Photos URLs
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'^my-photos/$', login_required(UserPhotosView.as_view()), name='user_photos'),
    url(r'^photos/$', PhotoListView.as_view(), name='photos_list'),
    url(r'^photos/(?P<pk>[0-9]+)$', DetailView.as_view(), name='photo_detail'),
    url(r'photos/new$', CreateView.as_view(), name='create_photo'),
]
