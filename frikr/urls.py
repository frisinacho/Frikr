"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from photos.views import HomeView, DetailView, CreateView, PhotoListView, UserPhotosView
from users.api import UserListAPI
from users.views import LoginView, LogoutView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Photo URLs
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'^my-photos/$', login_required(UserPhotosView.as_view()), name='user_photos'),
    url(r'^photos/$', PhotoListView.as_view(), name='photos_list'),
    url(r'^photos/(?P<pk>[0-9]+)$', DetailView.as_view(), name='photo_detail'),
    url(r'photos/new$', CreateView.as_view(), name='create_photo'),

    # User URLs
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),

    # User API URLs
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='user_list_api'),
]
