from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'index.html'


<<<<<<< HEAD
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
=======
def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })
>>>>>>> 8cccd1e2212f8f0c4d43492dc92044f75578c44a
