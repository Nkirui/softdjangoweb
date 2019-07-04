#from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import re_path



urlpatterns = [
    re_path(r'^home/$', views.home, name='home'),
   
]