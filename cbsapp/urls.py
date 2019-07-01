from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views




urlpatterns = [
    url(r'', views.index, name='index'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^profile/update/', views.update_profile, name='update_profile'),
]
