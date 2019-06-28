from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views




urlpatterns = [
     url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
     url(r'^profile/new/', views.new_profile, name='newProfileprofile'),
     url(r'^profile/updated', views.update_profile, name='updateProfile'),

]
