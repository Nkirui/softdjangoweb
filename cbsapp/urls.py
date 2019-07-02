from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .import views




urlpatterns = [
<<<<<<< HEAD

   url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
   url(r'^profile/update/', views.update_profile, name='update_profile'),



=======
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^profile/update/', views.update_profile, name='update_profile'),
>>>>>>> 39baf019258d43f170378ec0efdc36ccbbe25435
]
