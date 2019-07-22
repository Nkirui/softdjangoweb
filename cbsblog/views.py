from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog


def index(request):
    return render_to_response('index.html', {
        'posts': Blog.objects.all()[:5]
    })


def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })
