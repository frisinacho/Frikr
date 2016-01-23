from django.conf.urls import url
from users.views import LoginView, LogoutView


urlpatterns = [
    # User URLs
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
]
