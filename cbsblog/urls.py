from . import views
from django.urls import path

urlpatterns = [
<<<<<<< HEAD
    path('blog/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] 
=======
    re_path(r'^blog', views.index, name='index'),
    re_path(r'^blog/view/(?P<slug>[^\.]+).html', views.view_post, name='view_blog_post')

]
>>>>>>> 8cccd1e2212f8f0c4d43492dc92044f75578c44a
