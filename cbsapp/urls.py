from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views





urlpatterns = [

   #
   # path(r'user/(?P<username>\w+)/$', views.profile, name='profile'),
   # path('profile/update/', views.update_profile, name='update_profile'),
   # path('register/',views.register, name='register'),
    path(r'', views.home, name = 'home'),

]
