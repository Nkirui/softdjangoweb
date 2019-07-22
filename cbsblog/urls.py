from django.urls import path, re_path, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path(r'^blog', views.index, name='index'),
    re_path(r'^blog/view/(?P<slug>[^\.]+).html', views.view_post, name='view_blog_post')

]
