from django.urls import path, re_path, reverse
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from . import forms, views

urlpatterns = [
    re_path(r'^cbs/$', views.hom, name='hom'),
]
