from django.urls import path, re_path, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path(r'^blog', views.index, name='index'),
    
   # path('blog/(?p<pk>\w+)/', views.single_blog, name='view_post')
path('<slug:slug>/', views.BlogDetail.as_view(), name='view_post')
    
]


