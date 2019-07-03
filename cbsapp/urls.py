from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views




urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    path(r'^profile/update/', views.update_profile, name='update_profile'),
]
