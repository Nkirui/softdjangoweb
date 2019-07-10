from django.shortcuts import render_to_response,get_object_or_404,Http404
from .models import Blog
from django.views import generic



def index(request):
    return render_to_response('index.html', {
        'posts': Blog.objects.order_by('-posted_on')[:9]
 })

# def view_post(request, slug):   
#     return render_to_response('view_post.html', {
#         post': get_object_or_404(Blog, slug=slug)
   
        
#def detail(request, blog_id):
    #blogdetail = get_object_or_404(Blog, pk=blog_id)
    #return render(request, "cbsblog/detail.html", {'blog':blogdetail})

#def single_blog(request,pk):
    
    #try:
       # post =get_object_or_404(Blog,pk =pk)
    #except DoesNotExist:
       # raise Http404()
    #return render(request,'view_post.html',{'post':post})  


class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'view_post.html'        