from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views





urlpatterns = [

    path(r'', views.home, name = 'home'),
    path('create_profile/',views.create_profile, name='create_profile')

]
