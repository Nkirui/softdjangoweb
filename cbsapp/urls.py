from django.urls import path, re_path, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^user/', views.profile, name='profile'),
    # re_path(r'^profile/update/', views.update_profile, name='update_profile'),
]
